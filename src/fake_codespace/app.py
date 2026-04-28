"""Application entry point for the fake Codespace package."""

from typing import Optional

from .auth import AuthError, authenticate, generate_token, fetch_user_from_token
from .utils import format_message, normalize_email


def run_demo(username: str, password: str, token: Optional[str] = None) -> None:
    print(format_message("Starting fake Codespace demo", "DEBUG"))

    try:
        user = authenticate(username, password)
    except AuthError as exc:
        print(format_message(f"Authentication failed: {exc}", "ERROR"))
        return

    print(format_message(f"Authenticated user: {user.username}", "SUCCESS"))
    print(format_message(f"Normalized email: {normalize_email(user.email)}", "INFO"))

    token_value = token or generate_token(user.username)
    print(format_message(f"Session token: {token_value}", "INFO"))

    validated = fetch_user_from_token(token_value)
    if validated:
        print(format_message(f"Token belongs to {validated.username}", "SUCCESS"))
    else:
        print(format_message("Token validation failed", "ERROR"))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the fake Codespace Python demo.")
    parser.add_argument("username", help="Username to authenticate")
    parser.add_argument("password", help="Password for the user")
    parser.add_argument("--token", help="Optional pre-generated token")
    args = parser.parse_args()

    run_demo(args.username, args.password, args.token)
