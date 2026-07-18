"""
=========================================================
 AEVRION Programming Language v0.4
 Built-in Functions
=========================================================
"""


# =====================================================
# Print
# =====================================================

from src.colors import Colors as C


def builtin_print(*args):

    values = []

    for arg in args:
        values.append(str(arg))

    print()

    print(
        C.BRIGHT_GREEN +
        "➜ Output" +
        C.RESET
    )

    print(
        C.BRIGHT_WHITE +
        " ".join(values) +
        C.RESET
    )

    print()

    return None



# =====================================================
# Input
# =====================================================

def builtin_input(prompt=""):

    return input(str(prompt))



# =====================================================
# Length
# =====================================================

def builtin_len(value):

    return len(value)



# =====================================================
# Type
# =====================================================

def builtin_type(value):

    if value is None:
        return "null"

    if isinstance(value, bool):
        return "boolean"

    if isinstance(value, int):
        return "number"

    if isinstance(value, float):
        return "number"

    if isinstance(value, str):
        return "string"

    return "object"



# =====================================================
# Convert
# =====================================================

def builtin_str(value):

    return str(value)



def builtin_int(value):

    return int(value)



def builtin_float(value):

    return float(value)



# =====================================================
# Math
# =====================================================

def builtin_abs(value):

    return abs(value)



def builtin_max(*values):

    return max(values)



def builtin_min(*values):

    return min(values)



# =====================================================
# Builtin Registry
# =====================================================

BUILTINS = {

    "print": builtin_print,

    "input": builtin_input,

    "len": builtin_len,

    "type": builtin_type,

    "str": builtin_str,

    "int": builtin_int,

    "float": builtin_float,

    "abs": builtin_abs,

    "max": builtin_max,

    "min": builtin_min,
}
