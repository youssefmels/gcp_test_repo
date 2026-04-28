"""Utility helpers used in the fake Codespace demo."""

from typing import Any


def format_message(message: str, prefix: str = "INFO") -> str:
    return f"[{prefix}] {message.strip()}"


def normalize_email(email: str) -> str:
    return email.strip().lower()


def ensure_string(value: Any) -> str:
    if value is None:
        return ""
    return str(value)
