"""Fake Codespace package with a small auth and utilities demo."""

from .app import run_demo
from .auth import AuthError, User, authenticate, fetch_user_from_token, generate_token, validate_token
from .session import Session, SessionManager, get_session_manager
from .utils import format_message, normalize_email

__all__ = [
    "AuthError",
    "User",
    "authenticate",
    "fetch_user_from_token",
    "generate_token",
    "run_demo",
    "validate_token",
    "format_message",
    "normalize_email",
    "Session",
    "SessionManager",
    "get_session_manager",
]
