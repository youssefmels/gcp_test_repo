"""Tests for the session management module."""

import pytest
from datetime import datetime, timedelta

from fake_codespace.session import Session, SessionManager, get_session_manager
from fake_codespace.auth import User


def test_session_creation():
    """Test creating a new session."""
    user = User(username="alice", email="alice@example.com")
    session = Session(user=user, token="tkn_test_123")
    
    assert session.user.username == "alice"
    assert session.token == "tkn_test_123"
    assert session.is_valid()


def test_session_expiration():
    """Test session expiration."""
    user = User(username="alice", email="alice@example.com")
    session = Session(
        user=user, 
        token="tkn_test_123",
        expires_at=datetime.now() - timedelta(hours=1)  # Expired 1 hour ago
    )
    
    assert not session.is_valid()


def test_session_extend():
    """Test extending session expiration."""
    user = User(username="alice", email="alice@example.com")
    session = Session(
        user=user, 
        token="tkn_test_123",
        expires_at=datetime.now() + timedelta(minutes=5)
    )
    
    old_expiry = session.expires_at
    session.extend(hours=2)
    
    assert session.expires_at > old_expiry
    assert session.is_valid()


def test_session_manager_create_and_retrieve():
    """Test creating and retrieving sessions."""
    manager = SessionManager()
    user = User(username="bob", email="bob@example.com")
    token = "tkn_bob_456"
    
    session = manager.create_session(user, token)
    retrieved = manager.get_session(token)
    
    assert retrieved is not None
    assert retrieved.user.username == "bob"
    assert retrieved.token == token


def test_session_manager_invalid_session():
    """Test retrieving an invalid or expired session."""
    manager = SessionManager()
    user = User(username="alice", email="alice@example.com")
    token = "tkn_alice_789"
    
    # Create an expired session
    session = Session(
        user=user,
        token=token,
        expires_at=datetime.now() - timedelta(hours=1)
    )
    manager._sessions[token] = session
    
    retrieved = manager.get_session(token)
    assert retrieved is None
    # Expired session should be cleaned up
    assert token not in manager._sessions


def test_session_manager_invalidate():
    """Test invalidating a session."""
    manager = SessionManager()
    user = User(username="carol", email="carol@example.com")
    token = "tkn_carol_101"
    
    manager.create_session(user, token)
    assert manager.get_session(token) is not None
    
    invalidated = manager.invalidate_session(token)
    assert invalidated
    assert manager.get_session(token) is None


def test_session_manager_active_count():
    """Test counting active sessions."""
    manager = SessionManager()
    user1 = User(username="alice", email="alice@example.com")
    user2 = User(username="bob", email="bob@example.com")
    
    manager.create_session(user1, "tkn_alice_1")
    manager.create_session(user2, "tkn_bob_1")
    
    assert manager.get_active_sessions_count() == 2


def test_session_manager_list_active_users():
    """Test listing active users."""
    manager = SessionManager()
    user1 = User(username="alice", email="alice@example.com")
    user2 = User(username="bob", email="bob@example.com")
    
    manager.create_session(user1, "tkn_alice_1")
    manager.create_session(user2, "tkn_bob_1")
    
    active_users = manager.list_active_users()
    assert len(active_users) == 2
    assert "alice" in active_users
    assert "bob" in active_users


def test_get_session_manager():
    """Test getting the global session manager."""
    manager = get_session_manager()
    assert isinstance(manager, SessionManager)
