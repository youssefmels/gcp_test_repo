from fake_codespace.auth import AuthError, authenticate, fetch_user_from_token, generate_token, validate_token


def test_generate_and_validate_token():
    token = generate_token("alice")
    assert token.startswith("tkn_alice_")
    assert validate_token(token)


def test_authenticate_valid_user():
    user = authenticate("alice", "wonderland")
    assert user.username == "alice"
    assert user.email == "alice@example.com"


def test_authenticate_invalid_password():
    try:
        authenticate("alice", "wrongpass")
        assert False, "Expected AuthError"
    except AuthError as exc:
        assert "Invalid password" in str(exc)


def test_fetch_user_from_token():
    token = generate_token("bob")
    user = fetch_user_from_token(token)
    assert user is not None
    assert user.username == "bob"
