"""
=========================================================
 AEVRION Programming Language v0.4
 Abstract Syntax Tree Nodes
=========================================================
"""


# =========================================================
# Base Node
# =========================================================

class ASTNode:

    def __repr__(self):
        return self.__class__.__name__


# =========================================================
# Program
# =========================================================

class ProgramNode(ASTNode):

    def __init__(self, statements):

        self.statements = statements

    def __repr__(self):

        return f"Program({self.statements})"


# =========================================================
# Literals
# =========================================================

class NumberNode(ASTNode):

    def __init__(self, value):

        self.value = value


class StringNode(ASTNode):

    def __init__(self, value):

        self.value = value


class BooleanNode(ASTNode):

    def __init__(self, value):

        self.value = value


class NullNode(ASTNode):

    def __init__(self):

        self.value = None


# =========================================================
# Identifier
# =========================================================

class IdentifierNode(ASTNode):

    def __init__(self, name):

        self.name = name


# =========================================================
# Expressions
# =========================================================

class BinaryOperationNode(ASTNode):

    def __init__(self, left, operator, right):

        self.left = left
        self.operator = operator
        self.right = right


class UnaryOperationNode(ASTNode):

    def __init__(self, operator, value):

        self.operator = operator
        self.value = value


# =========================================================
# Variables
# =========================================================

class VariableDeclarationNode(ASTNode):

    def __init__(self, name, value):

        self.name = name
        self.value = value


class AssignmentNode(ASTNode):

    def __init__(self, name, value):

        self.name = name
        self.value = value


# =========================================================
# Statements
# =========================================================

class PrintNode(ASTNode):

    def __init__(self, value):

        self.value = value


class BlockNode(ASTNode):

    def __init__(self, statements):

        self.statements = statements


# =========================================================
# Conditions
# =========================================================

class IfNode(ASTNode):

    def __init__(
        self,
        condition,
        body,
        else_body=None
    ):

        self.condition = condition
        self.body = body
        self.else_body = else_body


# =========================================================
# Loops
# =========================================================

class WhileNode(ASTNode):

    def __init__(self, condition, body):

        self.condition = condition
        self.body = body


class ForNode(ASTNode):

    def __init__(
        self,
        variable,
        iterable,
        body
    ):

        self.variable = variable
        self.iterable = iterable
        self.body = body


# =========================================================
# Functions
# =========================================================

class FunctionNode(ASTNode):

    def __init__(
        self,
        name,
        parameters,
        body
    ):

        self.name = name
        self.parameters = parameters
        self.body = body


class CallNode(ASTNode):

    def __init__(
        self,
        function,
        arguments
    ):

        self.function = function
        self.arguments = arguments


class ReturnNode(ASTNode):

    def __init__(self, value):

        self.value = value
