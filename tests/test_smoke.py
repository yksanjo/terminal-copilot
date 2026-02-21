import importlib


def test_main_exists():
    mod = importlib.import_module("terminal_copilot.cli")
    assert hasattr(mod, "main")
