import os

from config import FILE_EXTENSION

def run_file(filename):

    if not os.path.exists(filename):
        print("Error: File not found.")
        return

    if not filename.endswith(FILE_EXTENSION):
        print("Error: Invalid AEVRION file.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    print("Running...")
    print("-" * 30)
    print(source)
    print("-" * 30)
    print("Program finished.")

