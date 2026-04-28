"""Session management for the fake Codespace demo."""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, Optional

from .auth import User


@dataclass
class Session:
    """Represents an active user session."""
    user: User
    token: str
    created_at: datetime = field(default_factory=datetime.now)
    expires_at: datetime = field(default_factory=lambda: datetime.now() + timedelta(hours=8))
    
    def is_valid(self) -> bool:
        """Check if the session is still valid."""
        return datetime.now() < self.expires_at
    
    def extend(self, hours: int = 1) -> None:
        """Extend the session expiration."""
        self.expires_at = datetime.now() + timedelta(hours=hours)


class SessionManager:
    """Manages user sessions."""
    
    def __init__(self):
        self._sessions: Dict[str, Session] = {}
    
    def create_session(self, user: User, token: str) -> Session:
        """Create a new session for a user."""
        session = Session(user=user, token=token)
        self._sessions[token] = session
        return session
    
    def get_session(self, token: str) -> Optional[Session]:
        """Retrieve a session by token, if valid."""
        session = self._sessions.get(token)
        if session and session.is_valid():
            return session
        elif session:
            # Clean up expired session
            del self._sessions[token]
        return None
    
    def invalidate_session(self, token: str) -> bool:
        """Invalidate a session."""
        if token in self._sessions:
            del self._sessions[token]
            return True
        return False
    
    def get_active_sessions_count(self) -> int:
        """Get the number of active sessions."""
        # Clean up expired sessions
        expired_tokens = [
            token for token, session in self._sessions.items()
            if not session.is_valid()
        ]
        for token in expired_tokens:
            del self._sessions[token]
        
        return len(self._sessions)
    
    def list_active_users(self) -> list[str]:
        """List all users with active sessions."""
        active_tokens = [
            token for token, session in self._sessions.items()
            if session.is_valid()
        ]
        # Update sessions list to remove expired ones
        for token in list(self._sessions.keys()):
            if not self._sessions[token].is_valid():
                del self._sessions[token]
        
        return [self._sessions[token].user.username for token in active_tokens]


# Global session manager instance
_session_manager = SessionManager()


def get_session_manager() -> SessionManager:
    """Get the global session manager instance."""
    return _session_manager
