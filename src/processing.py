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
    return [operation for operation in operations if operation.get("state") == state]
