"""
=========================================================
 AEVRION Programming Language v0.4
 Interactive Shell
=========================================================
"""

import os
import sys

from src.colors import Colors as C
from src.banner import print_aevrion_banner
from version import VERSION

from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter


# =====================================================
# Clear Screen
# =====================================================

def clear_screen():
    os.system("clear")


# =====================================================
# Help Menu
# =====================================================

def show_help():

    print()

    C.box("AEVRION COMMANDS", 40)

    print()

    print(C.BRIGHT_CYAN + "General" + C.RESET)
    print("  help         Show help")
    print("  clear        Clear screen")
    print("  banner       Show banner")
    print("  version      Show version")
    print("  about        About AEVRION")
    print("  exit         Exit AEVRION")

    print()

    print(C.BRIGHT_GREEN + "Language" + C.RESET)
    print("  herald EXPR          Display output")
    print("  let name = value     Create variable")

    print()

    print(C.BRIGHT_MAGENTA + "Operators" + C.RESET)
    print("  +   -   *   /   %")
    print("  >   <   >=   <=")
    print("  ==  !=")

    print()

    print(C.BRIGHT_YELLOW + "Examples" + C.RESET)
    print("  herald 10 + 20")
    print("  let age = 15")
    print("  herald age")

    print()

    print(
        C.DIM +
        "────────────────────────────────────────────────────────────" +
        C.RESET
    )

    print()

# =====================================================
# Start AEVRION Shell
# =====================================================

def start_shell(mode="core"):

    interpreter = Interpreter()

    clear_screen()

    print_aevrion_banner(mode)

    runtime = mode.lower() == "runtime"

    title = (
        "AEVRION RUNTIME"
        if runtime
        else "AEVRION CORE"
    )

    print(
        C.BRIGHT_GREEN +
        "System Ready." +
        C.RESET
    )

    print(
        C.DIM +
        "Enter 'help' to see available commands." +
        C.RESET
    )

    print()

    while True:

        try:

            print(
                C.BRIGHT_BLUE +
                f"┌─[ {title} ]" +
                C.RESET
            )

            command = input(
                C.BRIGHT_BLUE +
                "└─➜ " +
                C.RESET
            ).strip()

            print(C.RESET, end="")

            if command == "":
                continue

            # ==========================================
            # AEVRION v0.2 Compatibility
            # herald -> print()
            # ==========================================

            if command.startswith("herald "):

                expression = command[7:].strip()

                command = f"print({expression})"

            # ==========================================
            # Built-in Commands
            # ==========================================

            if command == "exit":

                print()

                print(
                    C.BRIGHT_YELLOW +
                    "Exiting AEVRION..." +
                    C.RESET
                )

                print()

                break

            elif command == "help":

                show_help()
                continue

            elif command == "clear":

                clear_screen()

                print_aevrion_banner(mode)

                print(
                    C.BRIGHT_GREEN +
                    "System Ready." +
                    C.RESET
                )

                print()

                continue

            elif command == "banner":

                print()

                print_aevrion_banner(mode)

                continue

            elif command == "version":

                print()

                print(
                    C.BRIGHT_CYAN +
                    f"AEVRION Programming Language {VERSION}" +
                    C.RESET
                )

                print()

                continue

            elif command == "about":

                print()

                C.box("ABOUT AEVRION", 32)

                print()

                print(
                    C.BRIGHT_WHITE +
                    "AEVRION Programming Language" +
                    C.RESET
                )

                print(
                    C.BRIGHT_CYAN +
                    "Version : " + VERSION +
                    C.RESET
                )

                print(
                    C.BRIGHT_GREEN +
                    "Created by Ashraful Ahmed" +
                    C.RESET
                )

                print()

                continue

            # ==========================================
            # Execute AEVRION Code
            # ==========================================

            try:

                lexer = Lexer(command)

                tokens = lexer.tokenize()

                parser = Parser(tokens)

                tree = parser.parse()

                result = interpreter.visit(tree)

                if result is not None:

                    print()

                    print(
                        C.BRIGHT_GREEN +
                        "➜ Output" +
                         C.RESET
                    )

                    print(
                        C.BRIGHT_WHITE +
                        str(result) +
                        C.RESET
                    )

                    print()

            except Exception as e:

                print()

                print(C.FAILURE)

                print(
                    C.BRIGHT_RED +
                    str(e) +
                    C.RESET
                )

                print()

                print(
                    C.BRIGHT_GREEN +
                    "Hint: Type 'help' for commands." +
                    C.RESET
                )

                print()

        except KeyboardInterrupt:

            print()

            print(C.INTERRUPTED)

            print()

            print(
                C.BRIGHT_YELLOW +
                "Use 'exit' to leave AEVRION." +
                C.RESET
            )

            print()

        except EOFError:

            print()

            print(
                C.BRIGHT_YELLOW +
                "Exiting AEVRION..." +
                C.RESET
            )

            print()

            break
