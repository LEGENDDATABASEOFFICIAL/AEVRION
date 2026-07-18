"""
=========================================================
 AEVRION Programming Language v0.4
 Lexer
=========================================================
"""

from src.tokens import *


class Lexer:

    def __init__(self, source, filename="<stdin>"):

        self.source = source
        self.filename = filename

        self.length = len(source)

        self.index = -1

        self.line = 1
        self.column = 0

        self.current_char = None

        self.advance()

    # =====================================================
    # Move Forward
    # =====================================================

    def advance(self):

        self.index += 1

        if self.index >= self.length:

            self.current_char = None
            return

        self.current_char = self.source[self.index]

        if self.current_char == "\n":

            self.line += 1
            self.column = 0

        else:

            self.column += 1

    # =====================================================
    # Look Ahead
    # =====================================================

    def peek(self):

        pos = self.index + 1

        if pos >= self.length:

            return None

        return self.source[pos]

    # =====================================================
    # Move Back
    # =====================================================

    def retreat(self):

        if self.index <= 0:

            return

        self.index -= 1

        self.current_char = self.source[self.index]

    # =====================================================
    # Current Position
    # =====================================================

    def position(self):

        return (
            self.line,
            self.column
        )

    # =====================================================
    # End Of File
    # =====================================================

    def eof(self):

        return self.current_char is None

    # =====================================================
    # Debug
    # =====================================================

    # =====================================================
    # Skip Whitespace
    # =====================================================

    def skip_whitespace(self):

        while self.current_char is not None and self.current_char in " \t\r\n":
            self.advance()

    # =====================================================
    # Read Identifier / Keyword
    # =====================================================

    def read_identifier(self):

        start_line = self.line
        start_column = self.column

        value = ""

        while (
            self.current_char is not None and
            (
                self.current_char.isalnum() or
                self.current_char == "_"
            )
        ):

            value += self.current_char
            self.advance()

        token_type = keyword_type(value)

        return Token(
            token_type,
            value,
            start_line,
            start_column
        )

    # =====================================================
    # Read Number
    # =====================================================

    def read_number(self):

        start_line = self.line
        start_column = self.column

        value = ""
        dot_count = 0

        while (
            self.current_char is not None and
            (
                self.current_char.isdigit() or
                self.current_char == "."
            )
        ):

            if self.current_char == ".":
                if dot_count == 1:
                    break

                dot_count += 1

            value += self.current_char
            self.advance()

        if dot_count == 0:
            number = int(value)
        else:
            number = float(value)

        return Token(
            NUMBER,
            number,
            start_line,
            start_column
        )


    # =====================================================
    # Read String
    # =====================================================

    def read_string(self):

        start_line = self.line
        start_column = self.column

        quote = self.current_char
        self.advance()

        value = ""

        escapes = {
            "n": "\n",
            "t": "\t",
            '"': '"',
            "'": "'",
            "\\": "\\"
        }

        while self.current_char is not None:

            if self.current_char == quote:
                self.advance()
                break

            if self.current_char == "\\":

                self.advance()

                if self.current_char is None:
                    break

                value += escapes.get(
                    self.current_char,
                    self.current_char
                )

                self.advance()
                continue

            value += self.current_char
            self.advance()

        return Token(
            STRING,
            value,
            start_line,
            start_column
        )

    # =====================================================
    # Skip Single Line Comment
    # =====================================================

    def skip_comment(self):

        while (
            self.current_char is not None and
            self.current_char != "\n"
        ):
            self.advance()

    # =====================================================
    # Skip Block Comment
    # =====================================================

    def skip_block_comment(self):

        self.advance()
        self.advance()

        while self.current_char is not None:

            if (
                self.current_char == "*" and
                self.peek() == "/"
            ):
                self.advance()
                self.advance()
                return

            self.advance()

    # =====================================================
    # Skip Blank Lines
    # =====================================================

    def skip_blank_lines(self):

        while (
            self.current_char is not None and
            self.current_char in "\n\r"
        ):
            self.advance()
     
        start_line = self.line
        start_column = self.column

        value = ""
        dot_count = 0

        while (
            self.current_char is not None and
            (
                self.current_char.isdigit() or
                self.current_char == "."
            )
        ):

            if self.current_char == ".":

                if dot_count == 1:
                    break

                dot_count += 1

            value += self.current_char
            self.advance()

        if dot_count == 0:
            number = int(value)
        else:
            number = float(value)

        return Token(
            NUMBER,
            number,
            start_line,
            start_column
        )

    # =====================================================
    # Read Operator
    # =====================================================

    def read_operator(self):

        start_line = self.line
        start_column = self.column

        ch = self.current_char

        # Two-character operators
        if ch == "=" and self.peek() == "=":
            self.advance()
            self.advance()
            return Token(EQ, "==", start_line, start_column)

        if ch == "!" and self.peek() == "=":
            self.advance()
            self.advance()
            return Token(NE, "!=", start_line, start_column)

        if ch == "<" and self.peek() == "=":
            self.advance()
            self.advance()
            return Token(LE, "<=", start_line, start_column)

        if ch == ">" and self.peek() == "=":
            self.advance()
            self.advance()
            return Token(GE, ">=", start_line, start_column)

        if ch == "&" and self.peek() == "&":
            self.advance()
            self.advance()
            return Token(AND, "&&", start_line, start_column)

        if ch == "|" and self.peek() == "|":
            self.advance()
            self.advance()
            return Token(OR, "||", start_line, start_column)

        if ch == "-" and self.peek() == ">":
            self.advance()
            self.advance()
            return Token(ARROW, "->", start_line, start_column)

        # Single-character operators
        operators = {
            "+": PLUS,
            "-": MINUS,
            "*": STAR,
            "/": SLASH,
            "%": MOD,
            "=": ASSIGN,
            "<": LT,
            ">": GT,
            "!": NOT,
        }

        if ch in operators:
            token = Token(
                operators[ch],
                ch,
                start_line,
                start_column
            )
            self.advance()
            return token

        return None

    # =====================================================
    # Read Symbol
    # =====================================================

    def read_symbol(self):

        start_line = self.line
        start_column = self.column

        symbols = {
            "(": LPAREN,
            ")": RPAREN,
            "{": LBRACE,
            "}": RBRACE,
            "[": LBRACKET,
            "]": RBRACKET,
            ",": COMMA,
            ".": DOT,
            ":": COLON,
            ";": SEMICOLON,
        }

        if self.current_char in symbols:

            token = Token(
                symbols[self.current_char],
                self.current_char,
                start_line,
                start_column
            )

            self.advance()

            return token

        return None
    # =====================================================
    # Tokenize Source Code
    # =====================================================

    def tokenize(self):

        tokens = []

        while self.current_char is not None:

            # Skip whitespace
            if self.current_char in " \t\r\n":
                self.skip_whitespace()
                continue

            # Single-line comment //
            if (
                self.current_char == "/" and
                self.peek() == "/"
            ):
                self.skip_comment()
                continue

            # Block comment /* */
            if (
                self.current_char == "/" and
                self.peek() == "*"
            ):
                self.skip_block_comment()
                continue

            # Identifier / Keyword
            if (
                self.current_char.isalpha() or
                self.current_char == "_"
            ):
                tokens.append(self.read_identifier())
                continue

            # Number
            if self.current_char.isdigit():
                tokens.append(self.read_number())
                continue

            # String
            if self.current_char in ('"', "'"):
                tokens.append(self.read_string())
                continue

            # Operator
            token = self.read_operator()

            if token is not None:
                tokens.append(token)
                continue

            # Symbol
            token = self.read_symbol()

            if token is not None:
                tokens.append(token)
                continue

            # Unknown character
            raise SyntaxError(
                f"Unexpected character '{self.current_char}' "
                f"at line {self.line}, column {self.column}"
            )

        tokens.append(
            Token(
                EOF,
                None,
                self.line,
                self.column
            )
        )

        return tokens

    # =====================================================
    # Read While
    # =====================================================

    def read_while(self, condition):

        text = ""

        while (
            self.current_char is not None and
            condition(self.current_char)
        ):

            text += self.current_char
            self.advance()

        return text

    def __repr__(self):

        return (
            f"<Lexer "
            f"line={self.line} "
            f"column={self.column} "
            f"char={repr(self.current_char)}>"
        )
