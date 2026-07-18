"""
=========================================================
 AEVRION Programming Language v0.4
 Advanced ANSI Color Engine
=========================================================
"""

class Colors:

    RESET = "\033[0m"

    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    PRIMARY = BRIGHT_CYAN
    SECONDARY = BRIGHT_MAGENTA
    SUCCESS = BRIGHT_GREEN
    WARNING = BRIGHT_YELLOW
    ERROR = BRIGHT_RED
    INFO = BRIGHT_BLUE

    TL = "╔"
    TR = "╗"
    BL = "╚"
    BR = "╝"
    HL = "═"
    VL = "║"

    STL = "┌"
    STR = "┐"
    SBL = "└"
    SBR = "┘"
    SH = "─"
    SV = "│"

    PROMPT_TOP = BRIGHT_BLUE + "┌─[" + RESET
    PROMPT_BOTTOM = BRIGHT_BLUE + "└─➜ " + RESET

    OK = BRIGHT_GREEN + "[✓]" + RESET
    ERROR_ICON = BRIGHT_RED + "[✖]" + RESET
    WARN = BRIGHT_YELLOW + "[!]" + RESET
    INFO_ICON = BRIGHT_CYAN + "[i]" + RESET

    OUTPUT = BRIGHT_GREEN + "➜ Output" + RESET
    FAILURE = BRIGHT_RED + "✖ ERROR" + RESET
    INTERRUPTED = BRIGHT_RED + "✖ INTERRUPTED" + RESET

    @staticmethod
    def box(title, width=36):
        print(
            Colors.PRIMARY +
            Colors.TL +
            Colors.HL * width +
            Colors.TR +
            Colors.RESET
        )
        print(
            Colors.PRIMARY +
            Colors.VL +
            title.center(width) +
            Colors.VL +
            Colors.RESET
        )
        print(
            Colors.PRIMARY +
            Colors.BL +
            Colors.HL * width +
            Colors.BR +
            Colors.RESET
        )
