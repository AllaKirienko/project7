from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    """Проверяет фильтрацию операций по статусу."""
    operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]

    result = filter_by_state(operations)

    assert result == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]


def test_filter_by_custom_state():
    """Проверяет фильтрацию с указанным статусом."""
    operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]

    result = filter_by_state(operations, "CANCELED")

    assert result == [
        {"id": 2, "state": "CANCELED"},
    ]


def test_sort_by_date():
    """Проверяет сортировку операций по дате."""
    operations = [
        {"date": "2023-01-01T10:00:00"},
        {"date": "2024-01-01T10:00:00"},
        {"date": "2022-01-01T10:00:00"},
    ]

    result = sort_by_date(operations)

    assert result == [
        {"date": "2024-01-01T10:00:00"},
        {"date": "2023-01-01T10:00:00"},
        {"date": "2022-01-01T10:00:00"},
    ]
