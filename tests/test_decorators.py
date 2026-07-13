from pathlib import Path

import pytest

from src.decorators import log


def test_log_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет вывод успешного выполнения функции в консоль."""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.out


def test_log_file(tmp_path: Path) -> None:
    """Проверяет запись успешного выполнения функции в файл."""

    file = tmp_path / "mylog.txt"

    @log(filename=str(file))
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(2, 3)

    assert result == 6
    assert file.read_text(encoding="utf-8") == "multiply ok"


def test_log_error_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет вывод ошибки функции в консоль."""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_error_file(tmp_path: Path) -> None:
    """Проверяет запись ошибки функции в файл."""

    file = tmp_path / "error.log"

    @log(filename=str(file))
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    text = file.read_text(encoding="utf-8")

    assert "divide error: ZeroDivisionError" in text
    assert "Inputs: (1, 0), {}" in text
