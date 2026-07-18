"""
=========================================================
 AEVRION Programming Language v0.4
 Interpreter
=========================================================
"""

from src.astnodes import *
from src.environment import Environment
from src.tokens import *
from src.builtins import BUILTINS


class Interpreter:


    def __init__(self):

        self.environment = Environment()



    # =====================================================
    # Execute Node
    # =====================================================

    def visit(self, node):

        method_name = (
            "visit_" +
            node.__class__.__name__
        )

        method = getattr(
            self,
            method_name,
            None
        )


        if method is None:

            raise Exception(
                f"No interpreter for {node.__class__.__name__}"
            )


        return method(node)



    # =====================================================
    # Program
    # =====================================================

    def visit_ProgramNode(self, node):

        result = None

        for statement in node.statements:

            result = self.visit(statement)

        return result



    # =====================================================
    # Numbers
    # =====================================================

    def visit_NumberNode(self, node):

        return node.value



    # =====================================================
    # Strings
    # =====================================================

    def visit_StringNode(self, node):

        return node.value



    # =====================================================
    # Boolean
    # =====================================================

    def visit_BooleanNode(self, node):

        return node.value



    # =====================================================
    # Null
    # =====================================================

    def visit_NullNode(self, node):

        return None



    # =====================================================
    # Identifier
    # =====================================================

    def visit_IdentifierNode(self, node):

        return self.environment.get(
            node.name
        )


    # =====================================================
    # Function Call
    # =====================================================

    def visit_CallNode(self, node):

        if not isinstance(node.function, IdentifierNode):
            raise Exception("Invalid function call.")

        name = node.function.name

        if name not in BUILTINS:
            raise Exception(f"Unknown function '{name}'")

        values = []

        for argument in node.arguments:
            values.append(
                self.visit(argument)
            )

        return BUILTINS[name](*values)


    # =====================================================
    # Variable Declaration
    # =====================================================

    def visit_VariableDeclarationNode(self, node):

        value = self.visit(
            node.value
        )

        self.environment.define(
            node.name,
            value
        )

        return value



    # =====================================================
    # Binary Operations
    # =====================================================

    def visit_BinaryOperationNode(self, node):

        left = self.visit(
            node.left
        )

        right = self.visit(
            node.right
        )


        op = node.operator


        if op == PLUS:
            return left + right

        if op == MINUS:
            return left - right

        if op == STAR:
            return left * right

        if op == SLASH:
            return left / right

        if op == MOD:
            return left % right


        if op == EQ:
            return left == right

        if op == NE:
            return left != right

        if op == LT:
            return left < right

        if op == GT:
            return left > right

        if op == LE:
            return left <= right

        if op == GE:
            return left >= right


        raise Exception(
            f"Unknown operator {op}"
        )
