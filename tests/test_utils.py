from fake_codespace.utils import ensure_string, format_message, normalize_email


def test_format_message():
    assert format_message("hello", "WARN") == "[WARN] hello"


def test_normalize_email():
    assert normalize_email("  UsEr@Example.COM  ") == "user@example.com"


def test_ensure_string():
    assert ensure_string(123) == "123"
    assert ensure_string(None) == ""
