from fake_codespace.app import run_demo


def test_run_demo_valid_user(capsys):
    run_demo("carol", "qwerty123")
    captured = capsys.readouterr()
    assert "Authenticated user: carol" in captured.out
    assert "Token belongs to carol" in captured.out
