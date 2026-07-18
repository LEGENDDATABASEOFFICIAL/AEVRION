from config import PROMPT

def start_repl():
    print()
    print("AEVRION Interactive Shell")
    print("Type 'exit' to quit.")
    print()

    while True:
        try:
            code = input(PROMPT)

            if not code.strip():
                continue

            if code.lower() == "exit":
                print("Goodbye.")
                break

            print("You entered:", code)

        except KeyboardInterrupt:
            print("\nInterrupted.")
            break

        except EOFError:
            print()
            break

