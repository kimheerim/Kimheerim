import builtins
import sys
from pathlib import Path

# Ensure the project root is on the Python path so the module can be imported
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import minor_or_adult


def test_is_adult_true():
    assert minor_or_adult.is_adult(18)
    assert minor_or_adult.is_adult(20)


def test_is_adult_false():
    assert not minor_or_adult.is_adult(17)


def test_main_adult(monkeypatch, capsys):
    inputs = iter(["Alice", "20"])
    minor_or_adult.main(input_func=lambda _: next(inputs))
    captured = capsys.readouterr()
    assert "Hello Alice. You are an adult." in captured.out


def test_main_minor_with_retry(monkeypatch, capsys):
    inputs = iter(["Bob", "abc", "15"])
    minor_or_adult.main(input_func=lambda _: next(inputs))
    captured = capsys.readouterr()
    assert "Please enter a valid integer for age." in captured.out
    assert "Hello Bob. You are a minor." in captured.out
