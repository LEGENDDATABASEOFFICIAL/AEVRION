#!/usr/bin/env python3

"""
=========================================
AEVRION Programming Language v0.4
Main Launcher
=========================================
"""

import sys

from src.runtime import Runtime
from src.shell import start_shell


def main():

    runtime = Runtime()
    runtime.startup()

    mode = "core"

    # Runtime Mode (-r)
    if len(sys.argv) > 1:
        if sys.argv[1] == "-r":
            mode = "runtime"

    try:
        start_shell(mode)

    except KeyboardInterrupt:
        print()

    finally:
        runtime.shutdown()


if __name__ == "__main__":
    main()
