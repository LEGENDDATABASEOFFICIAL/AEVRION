"""
=========================================================
 AEVRION Programming Language v0.4
 Banner
=========================================================
"""

from src.colors import Colors as C
from version import VERSION, AUTHOR


def print_aevrion_banner(mode="core"):
    print()

    banner = [
    (C.BRIGHT_RED,     " █████╗ ███████╗██╗   ██╗██████╗ ██╗ ██████╗ ███╗   ██╗"),
    (C.BRIGHT_YELLOW,  "██╔══██╗██╔════╝██║   ██║██╔══██╗██║██╔═══██╗████╗  ██║"),
    (C.BRIGHT_GREEN,   "███████║█████╗  ██║   ██║██████╔╝██║██║   ██║██╔██╗ ██║"),
    (C.BRIGHT_CYAN,    "██╔══██║██╔══╝  ╚██╗ ██╔╝██╔══██╗██║██║   ██║██║╚██╗██║"),
    (C.BRIGHT_BLUE,    "██║  ██║███████╗ ╚████╔╝ ██║  ██║██║╚██████╔╝██║ ╚████║"),
    (C.BRIGHT_MAGENTA, "╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝"),

    (C.BRIGHT_WHITE, ""),
    (C.BRIGHT_WHITE,   "              ⚡ A E V R I O N ⚡"),
    (C.BRIGHT_CYAN,    "     Modern • Fast • Powerful Programming Language"),
    (C.BRIGHT_WHITE, ""),
]

    for color, line in banner:
        print(C.BOLD + color + line + C.RESET)

    print()
    print(C.BRIGHT_WHITE + f"AEVRION Programming Language {VERSION}" + C.RESET)
    print(C.BRIGHT_CYAN + f"Author: {AUTHOR}" + C.RESET)

    if mode.lower() == "runtime":
        build = "v0.4 Runtime Edition"
        mode_text = "Runtime"
    else:
        build = "v0.4 Logic Edition"
        mode_text = "Logic"

    print(C.BRIGHT_MAGENTA + f"Build: {build}" + C.RESET)
    print(C.BRIGHT_YELLOW + f"Mode : {mode_text}" + C.RESET)

    print()
    print(C.DIM + "Type 'help' for commands | 'exit' to quit" + C.RESET)
    print()

    title = "AEVRION RUNTIME" if mode.lower() == "runtime" else "AEVRION CORE"
    C.box(title)

    print()
    print(C.OK + " CORE    : ONLINE")
    print(C.OK + " LEXER   : READY")
    print(C.OK + " PARSER  : READY")
    print(C.OK + " ENGINE  : READY")

    if mode.lower() == "runtime":
        print(C.OK + " RUNTIME : READY")
        print(C.OK + " BUFFER  : EMPTY")
        print()
        print(C.BRIGHT_YELLOW + "Entering Runtime Mode..." + C.RESET)
    else:
        print()
        print(C.BRIGHT_GREEN + "AEVRION Core initialized successfully." + C.RESET)

    print()
    print(C.DIM + "────────────────────────────────────────────────────────────────────────────────" + C.RESET)
    print()
