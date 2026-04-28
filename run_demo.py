"""Root helper script for running the fake Codespace demo from the repository root."""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from fake_codespace.app import run_demo


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the fake Codespace demo from the repository root.")
    parser.add_argument("username", help="Username to authenticate")
    parser.add_argument("password", help="Password for the user")
    parser.add_argument("--token", help="Optional pre-generated token")
    args = parser.parse_args()

    run_demo(args.username, args.password, args.token)


if __name__ == "__main__":
    main()
