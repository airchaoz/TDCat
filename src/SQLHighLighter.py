"""
Licensed under the GNU General Public License
File: SQLHighLighter.py
Author: jplozf <jpl@ozf.fr>
"""

from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtGui import QSyntaxHighlighter
from PyQt5.QtGui import QTextCharFormat


class SQLHighLighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(SQLHighLighter, self).__init__(parent)

        # liste des règles: [[regex, format], [regex, format], ...]
        self.regles = []

        # --------------------------------------------------------------------
        # coloration des mots clés SQL de sqlite3
        motcles_format = QTextCharFormat()
        motcles_format.setForeground(QColor("#097BF7"))  # mots clés en bleu
        motcles_format.setFontWeight(QFont.Bold)  # pour mise en gras
        # liste des mots à considérer
        motcles_motifs = [
            "ABORT",
            "ACTION",
            "ADD",
            "AFTER",
            "ALL",
            "ALTER",
            "ANALYZE",
            "AND",
            "AS",
            "ASC",
            "ATTACH",
            "AUTOINCREMENT",
            "BEFORE",
            "BEGIN",
            "BETWEEN",
            "BY",
            "CASCADE",
            "CASE",
            "CAST",
            "CHECK",
            "COLLATE",
            "COLUMN",
            "COMMIT",
            "CONFLICT",
            "CONSTRAINT",
            "CREATE",
            "CROSS",
            "CURRENT_DATE",
            "CURRENT_TIME",
            "CURRENT_TIMESTAMP",
            "DATABASE",
            "DEFAULT",
            "DEFERRABLE",
            "DEFERRED",
            "DELETE",
            "DESC",
            "DETACH",
            "DISTINCT",
            "DROP",
            "EACH",
            "ELSE",
            "END",
            "ESCAPE",
            "EXCEPT",
            "EXCLUSIVE",
            "EXISTS",
            "EXPLAIN",
            "FAIL",
            "FOR",
            "FOREIGN",
            "FROM",
            "FULL",
            "GLOB",
            "GROUP",
            "HAVING",
            "IF",
            "IGNORE",
            "IMMEDIATE",
            "IN",
            "INDEX",
            "INDEXED",
            "INITIALLY",
            "INNER",
            "INSERT",
            "INSTEAD",
            "INTERSECT",
            "INTO",
            "IS",
            "ISNULL",
            "JOIN",
            "KEY",
            "LEFT",
            "LIKE",
            "LIMIT",
            "MATCH",
            "NATURAL",
            "NO",
            "NOT",
            "NOTNULL",
            "NULL",
            "OF",
            "OFFSET",
            "ON",
            "OR",
            "ORDER",
            "OUTER",
            "PLAN",
            "PRAGMA",
            "PRIMARY",
            "QUERY",
            "RAISE",
            "RECURSIVE",
            "REFERENCES",
            "REGEXP",
            "REINDEX",
            "RELEASE",
            "RENAME",
            "REPLACE",
            "RESTRICT",
            "RIGHT",
            "ROLLBACK",
            "ROW",
            "SAVEPOINT",
            "SELECT",
            "SET",
            "TABLE",
            "TEMP",
            "TEMPORARY",
            "THEN",
            "TO",
            "TRANSACTION",
            "TRIGGER",
            "UNION",
            "UNIQUE",
            "UPDATE",
            "USING",
            "VACUUM",
            "VALUES",
            "VIEW",
            "VIRTUAL",
            "WHEN",
            "WHERE",
            "WITH",
            "WITHOUT",
        ]
        motcles_motifs += ["TEXT", "INTEGER", "REAL", "NUMERIC", "NONE", "BLOB"]
        motcles_motifs += ["TRUE", "FALSE"]
        # enregistrement dans la liste des règles
        for motcles_motif in motcles_motifs:
            motcles_regex = QRegExp("\\b" + motcles_motif + "\\b", Qt.CaseInsensitive)
            self.regles.append([motcles_regex, motcles_format])

        # --------------------------------------------------------------------
        # nombre entier ou flottant
        nombre_format = QTextCharFormat()
        nombre_format.setForeground(QColor("#66C853"))
        nombre_motif = "\\b[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?\\b"
        nombre_regex = QRegExp(nombre_motif)
        nombre_regex.setMinimal(True)
        self.regles.append([nombre_regex, nombre_format])

        # --------------------------------------------------------------------
        # chaine de caractères simple quote: '...'
        chaine1_format = QTextCharFormat()
        chaine1_format.setForeground(QColor("#66C853"))  # red)
        chaine1_motif = "'.*'"
        chaine1_regex = QRegExp(chaine1_motif)
        chaine1_regex.setMinimal(True)
        self.regles.append([chaine1_regex, chaine1_format])

        # --------------------------------------------------------------------
        # chaine de caractères double quotes: "..."
        chaine2_format = QTextCharFormat()
        chaine2_motif = '".*"'
        chaine2_regex = QRegExp(chaine2_motif)
        chaine2_regex.setMinimal(True)
        self.regles.append([chaine2_regex, chaine2_format])

        # --------------------------------------------------------------------
        # delimiteur: parenthèses, crochets, accolades
        delimiteur_format = QTextCharFormat()
        delimiteur_motif = "[\)\(]+|[\{\}]+|[][]+"
        delimiteur_regex = QRegExp(delimiteur_motif)
        self.regles.append([delimiteur_regex, delimiteur_format])

        # --------------------------------------------------------------------
        # commentaire sur une seule ligne et jusqu'à fin de ligne: --...\n
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.gray)
        comment_motif = "--[^\n]*"
        comment_regex = QRegExp(comment_motif)
        self.regles.append([comment_regex, comment_format])

        # --------------------------------------------------------------------
        # commentaires multi-lignes: /*...*/
        self.commentml_format = QTextCharFormat()
        self.commentml_format.setForeground(Qt.gray)

        self.commentml_deb_regex = QRegExp("/\\*")
        self.commentml_fin_regex = QRegExp("\\*/")

    # ========================================================================
    def highlightBlock(self, text):
        """analyse chaque ligne et applique les règles"""

        # analyse des lignes avec les règles
        for expression, tformat in self.regles:
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, tformat)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # pour les commentaires multilignes: /* ... */
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentml_deb_regex.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentml_fin_regex.indexIn(text, startIndex)
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentml_lg = len(text) - startIndex
            else:
                commentml_lg = (
                    endIndex - startIndex + self.commentml_fin_regex.matchedLength()
                )

            self.setFormat(startIndex, commentml_lg, self.commentml_format)

            startIndex = self.commentml_deb_regex.indexIn(
                text, startIndex + commentml_lg
            )