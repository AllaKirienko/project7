import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations() -> list[dict[str, str]]:
    """Возвращает список операций для тестирования."""
    return [
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2024-01-01T10:00:00",
        },
        {
            "id": "2",
            "state": "CANCELED",
            "date": "2023-01-01T10:00:00",
        },
        {
            "id": "3",
            "state": "EXECUTED",
            "date": "2022-01-01T10:00:00",
        },
    ]


def test_filter_by_state(operations: list[dict[str, str]]) -> None:
    """Проверяет фильтрацию операций по статусу EXECUTED."""
    result = filter_by_state(operations)

    assert len(result) == 2
    assert result[0]["state"] == "EXECUTED"
    assert result[1]["state"] == "EXECUTED"


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 0),
    ],
)
def test_filter_by_state_parametrized(
    operations: list[dict[str, str]], state: str, expected_count: int
) -> None:
    """Проверяет фильтрацию операций с разными статусами."""
    result = filter_by_state(operations, state)

    assert len(result) == expected_count


def test_sort_by_date(operations: list[dict[str, str]]) -> None:
    """Проверяет сортировку операций по дате."""
    result = sort_by_date(operations)

    assert result[0]["date"] == "2024-01-01T10:00:00"
    assert result[-1]["date"] == "2022-01-01T10:00:00"