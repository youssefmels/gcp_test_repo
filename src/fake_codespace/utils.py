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

def send_notification(email: str, message: str) -> bool:
    """Send a notification email to a user.
    
    NOTE: Interface under review - may need to be refactored to accept
    template_type and context dict instead of raw message string.
    Current callers should not finalize integration until interface is confirmed.
    """
    if not email or not isinstance(message, str):
        return False
    normalized = normalize_email(email)
    # TODO: replace with actual email service call
    print(format_message(f"Sending notification to {normalized}: {message}", "INFO"))
    return True