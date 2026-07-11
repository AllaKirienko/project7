from datetime import datetime
from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """
    Возвращает список операций с указанным статусом.

    :param operations: список банковских операций.
    :param state: статус операции для фильтрации.
                  По умолчанию "EXECUTED".
    :return: новый список операций с указанным статусом.
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == state
    ]


def sort_by_date(
    operations: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """
    Сортирует операции по дате.

    :param operations: список банковских операций.
    :param reverse: порядок сортировки.
                    По умолчанию True — сначала новые даты.
    :return: новый отсортированный список операций.
    """
    return sorted(
        operations,
        key=lambda operation: datetime.fromisoformat(operation["date"]),
        reverse=reverse,
    )
