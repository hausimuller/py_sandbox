#!/usr/bin/env python3
"""
module_name.py

Brief description of what this module does.
"""

import sys
# import other standard or third-party libraries here

def main(argv=None):
    """
    The main entry point of the script.
    :param argv: list of command-line arguments (defaults to sys.argv)
    """
    if argv is None:
        argv = sys.argv[1:]
    # Your script logic here
    print("Arguments received:", argv)
    # … more functionality …

if __name__ == "__main__":
    # When run as a script, call main() and exit with its return code (if any)
    exit_code = main()
    # If main() returns an integer, use it as the exit code; otherwise default to 0
    if isinstance(exit_code, int):
        sys.exit(exit_code)
