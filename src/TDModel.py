from taosrest import connect
import json
from TDCommon import PAGE_SIZE
from math import ceil


class TCConnectException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TDConnect:
    def __init__(self, name, url, port, user, password, timeout=30) -> None:
        self._comm: connect = None
        self.name = name
        self.url = url
        self.port = port
        self.user = user
        self.password = password
        self.timeout = timeout

        self.db_dict = dict()

    def connect_init(self) -> None:
        try:
            self._comm = connect(
                url=f"{self.url}:{self.port}",
                user=self.user,
                password=self.password,
                timeout=int(self.timeout),
            )
        except Exception as e:
            self._comm = None
            raise TCConnectException(e)

    def db_init(self) -> None:
        if not self._comm:
            return
        rsp = self._comm.query("show databases")
        for item in rsp:
            db_name = item[0]
            self.db_dict[db_name] = TDDBModel(db_name, self._comm)

    def get_td_version(self) -> str:
        if not self._comm:
            return ""

        return self._comm.server_info

    def is_activate(self) -> bool:
        return len(self.db_dict) > 0

    def refresh(self) -> None:
        self.db_init()

    def config_dump(self) -> str:
        config = {
            "name": self.name,
            "url": self.url,
            "port": self.port,
            "user": self.user,
            "password": self.password,
            "timeout": self.timeout,
        }
        return json.dumps(config)

    def get_params(self):
        return self.url, self.port, self.user, self.password, self.name


class TDDBModel:
    def __init__(self, db_name: str, comm: connect) -> None:
        self.db_name: str = db_name
        self._comm: connect = comm

        self.table_dict = dict()
        self.stable_dict = dict()

    def init(self):
        self.init_stable()
        self.init_table()

    def init_table(self):
        if not self._comm:
            return
        rsp = self._comm.query(f"show {self.db_name}.tables;")
        for item in rsp:
            table_name = item[0]
            self.table_dict[table_name] = TDTableModel(
                self.db_name, table_name, self._comm
            )

    def init_stable(self):
        if not self._comm:
            return
        rsp = self._comm.query(f"show {self.db_name}.stables;")
        for item in rsp:
            table_name = item[0]
            self.stable_dict[table_name] = TDStableModel(
                self.db_name, table_name, self._comm
            )


class TDTableModel:
    def __init__(self, db_name: str, table_name: str, comm: connect) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._comm = comm

    def query(self, page=0):
        if not self._comm:
            return
        rsp = self._comm.query(
            f"select * from {self.db_name}.{self.table_name} limit {int(page*PAGE_SIZE)}, {int(PAGE_SIZE+page*PAGE_SIZE)};"
        )

        fields = [i["name"] for i in rsp.fields]

        return fields, rsp.data

    def query_pages(self):
        if not self._comm:
            return 0
        rsp = self._comm.query(
            f"select count(*) from {self.db_name}.{self.table_name};"
        )
        return ceil(rsp.data[0][0] / PAGE_SIZE)


class TDStableModel:
    def __init__(self, db_name: str, stable_name: str, comm: connect) -> None:
        self.db_name = db_name
        self.table_name = stable_name
        self._comm = comm


if __name__ == "__main__":
    td = TDConnect("http://127.0.0.1:3000", "root", "taosdata")
    td.connect_init()
    td.db_init()