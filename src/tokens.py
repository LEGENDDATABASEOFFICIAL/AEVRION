"""
=========================================================
 AEVRION Programming Language v0.4
 Token Definitions
=========================================================
"""

from dataclasses import dataclass

# =========================================================
# TOKEN TYPES
# =========================================================

# Literals
NUMBER = "NUMBER"
STRING = "STRING"
IDENTIFIER = "IDENTIFIER"

# Keywords
LET = "LET"
CONST = "CONST"
FUNC = "FUNC"
RETURN = "RETURN"

IF = "IF"
ELSE = "ELSE"

FOR = "FOR"
WHILE = "WHILE"

BREAK = "BREAK"
CONTINUE = "CONTINUE"

CLASS = "CLASS"

IMPORT = "IMPORT"

TRUE = "TRUE"
FALSE = "FALSE"
NULL = "NULL"

# Operators
PLUS = "PLUS"
MINUS = "MINUS"
STAR = "STAR"
SLASH = "SLASH"
MOD = "MOD"

ASSIGN = "ASSIGN"

EQ = "EQ"
NE = "NE"

LT = "LT"
GT = "GT"
LE = "LE"
GE = "GE"

AND = "AND"
OR = "OR"
NOT = "NOT"

# Symbols
LPAREN = "LPAREN"
RPAREN = "RPAREN"

LBRACE = "LBRACE"
RBRACE = "RBRACE"

LBRACKET = "LBRACKET"
RBRACKET = "RBRACKET"

COMMA = "COMMA"
DOT = "DOT"
COLON = "COLON"
SEMICOLON = "SEMICOLON"

ARROW = "ARROW"

NEWLINE = "NEWLINE"

EOF = "EOF"

# =========================================================
# KEYWORDS
# =========================================================

KEYWORDS = {

    "let": LET,
    "const": CONST,

    "func": FUNC,
    "return": RETURN,

    "if": IF,
    "else": ELSE,

    "for": FOR,
    "while": WHILE,

    "break": BREAK,
    "continue": CONTINUE,

    "class": CLASS,

    "import": IMPORT,

    "true": TRUE,
    "false": FALSE,
    "null": NULL,
}

# =========================================================
# TOKEN OBJECT
# =========================================================

@dataclass
class Token:

    type: str
    value: object
    line: int
    column: int

    def __str__(self):
        return f"{self.type}({self.value})"

    def __repr__(self):
        return self.__str__()

# =========================================================
# HELPERS
# =========================================================

def is_keyword(word):

    return word in KEYWORDS


def keyword_type(word):

    return KEYWORDS.get(word, IDENTIFIER)


def make_token(token_type, value, line, column):

    return Token(token_type, value, line, column)
