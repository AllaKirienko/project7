from typing import Iterator


def filter_by_currency(
    transactions: list[dict], currency: str
) -> Iterator[dict]:
    """Возвращает операции с указанной валютой.

    Args:
        transactions: Список банковских операций.
        currency: Код валюты для фильтрации.

    Returns:
        Итератор операций с указанной валютой.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(
    transactions: list[dict],
) -> Iterator[str]:
    """Возвращает описания банковских операций по очереди.

    Args:
        transactions: Список банковских операций.

    Returns:
        Итератор с описаниями операций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start: Начальный номер карты.
        stop: Конечный номер карты.

    Returns:
        Итератор номеров карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)
        yield " ".join(
            [
                card_number[:4],
                card_number[4:8],
                card_number[8:12],
                card_number[12:16],
            ]
        )
