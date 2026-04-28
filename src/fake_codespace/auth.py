"""Authentication utilities for the fake Codespace demo."""

from dataclasses import dataclass
import secrets
from typing import Dict, Optional


@dataclass(frozen=True)
class User:
    username: str
    email: str


class AuthError(Exception):
    pass


_USER_DB: Dict[str, str] = {
    "alice": "wonderland",
    "bob": "builder",
    "carol": "qwerty123",
}


def generate_token(username: str) -> str:
    token = secrets.token_urlsafe(18)
    return f"tkn_{username}_{token}"


def validate_token(token: str) -> bool:
    return isinstance(token, str) and token.startswith("tkn_") and len(token) > 20


def authenticate(username: str, password: str) -> User:
    if username not in _USER_DB:
        raise AuthError("Unknown user")

    expected = _USER_DB[username]
    if password != expected:
        raise AuthError("Invalid password")

    return User(username=username, email=f"{username}@example.com")


def fetch_user_from_token(token: str) -> Optional[User]:
    if not validate_token(token):
        return None

    parts = token.split("_")
    if len(parts) < 3:
        return None

    username = parts[1]
    if username not in _USER_DB:
        return None

    return User(username=username, email=f"{username}@example.com")
