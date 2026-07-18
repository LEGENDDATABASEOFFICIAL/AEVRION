"""
=========================================================
 AEVRION Programming Language v0.4
 Parser
=========================================================
"""

from src.tokens import *
from src.astnodes import *


class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.index = -1
        self.current_token = None

        self.advance()


    # =====================================================
    # Move Forward
    # =====================================================

    def advance(self):

        self.index += 1

        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]

        return self.current_token


    # =====================================================
    # Look Ahead
    # =====================================================

    def peek(self):

        pos = self.index + 1

        if pos >= len(self.tokens):
            return None

        return self.tokens[pos]


    # =====================================================
    # Check Token
    # =====================================================

    def check(self, token_type):

        return (
            self.current_token.type == token_type
        )


    # =====================================================
    # Consume Token
    # =====================================================

    def consume(self, token_type):

        if self.check(token_type):

            token = self.current_token
            self.advance()
            return token


        raise Exception(
            f"Expected {token_type}, "
            f"got {self.current_token.type}"
        )


    # =====================================================
    # Parse Entry
    # =====================================================

    def parse(self):

        return self.parse_program()



    # =====================================================
    # Parse Expression
    # =====================================================

    def parse_expression(self):

        token = self.current_token

        # Number
        if token.type == NUMBER:

            self.advance()
            return NumberNode(token.value)

        # String
        if token.type == STRING:

            self.advance()
            return StringNode(token.value)

        # True
        if token.type == TRUE:

            self.advance()
            return BooleanNode(True)

        # False
        if token.type == FALSE:

            self.advance()
            return BooleanNode(False)

        # Null
        if token.type == NULL:

            self.advance()
            return NullNode()

        # Identifier / Function Call
        if token.type == IDENTIFIER:

            name = token.value
            self.advance()

            if self.current_token is not None and self.current_token.type == LPAREN:

                self.advance()

                arguments = []

                if self.current_token.type != RPAREN:

                    arguments.append(
                        self.parse_binary_expression()
                    )

                    while self.current_token.type == COMMA:

                        self.advance()

                        arguments.append(
                            self.parse_binary_expression()
                        )

                self.consume(RPAREN)

                return CallNode(
                    IdentifierNode(name),
                    arguments
                )

            return IdentifierNode(name)

        # Parentheses
        if token.type == LPAREN:

            self.advance()

            expression = self.parse_binary_expression()

            self.consume(RPAREN)

            return expression

        raise Exception(
            f"Unexpected token: {token}"
        )


    # =====================================================
    # Parse Variable Declaration
    # =====================================================

    def parse_variable_declaration(self):

        # consume 'let'

        self.consume(LET)


        # variable name

        name = self.consume(
            IDENTIFIER
        )


        # equals sign

        self.consume(
            ASSIGN
        )


        # value expression

        value = self.parse_expression()


        return VariableDeclarationNode(
            name.value,
            value
        )

   # =====================================================
    # Parse Statement
    # =====================================================

    def parse_statement(self):

        # Variable declaration
        if self.current_token.type == LET:

            return self.parse_variable_declaration()


        # Expression statement
        return self.parse_binary_expression()



    # =====================================================
    # Parse Full Program
    # =====================================================

    def parse_program(self):

        statements = []

        while not self.check(EOF):

            statements.append(
                self.parse_statement()
            )


        return ProgramNode(statements)

# =====================================================
    # Parse Statement
    # =====================================================

    def parse_statement(self):

        # Variable declaration
        if self.current_token.type == LET:

            return self.parse_variable_declaration()


        # Expression statement
        return self.parse_binary_expression()



    # =====================================================
    # Parse Full Program
    # =====================================================

    def parse_program(self):

        statements = []

        while not self.check(EOF):

            statements.append(
                self.parse_statement()
            )


        return ProgramNode(statements)

    # =====================================================
    # Parse Binary Operations
    # =====================================================

    def parse_binary_expression(self, min_priority=0):

        left = self.parse_expression()


        priorities = {

            OR: 1,
            AND: 2,

            EQ: 3,
            NE: 3,

            LT: 4,
            GT: 4,
            LE: 4,
            GE: 4,

            PLUS: 5,
            MINUS: 5,

            STAR: 6,
            SLASH: 6,
            MOD: 6
        }


        while (
            self.current_token.type in priorities and
            priorities[self.current_token.type] >= min_priority
        ):

            operator = self.current_token

            priority = priorities[operator.type]

            self.advance()


            right = self.parse_binary_expression(
                priority + 1
            )


            left = BinaryOperationNode(
                left,
                operator.type,
                right
            )


        return left
