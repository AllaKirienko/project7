import pytest

from src.generators.generators import (card_number_generator,
                                       filter_by_currency,
                                       transaction_descriptions)


@pytest.fixture
def transactions() -> list[dict]:
    """Возвращает список операций для тестирования."""
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "100",
                "currency": {
                    "code": "USD",
                },
            },
        },
        {
            "id": 2,
            "description": "Покупка продуктов",
            "operationAmount": {
                "amount": "200",
                "currency": {
                    "code": "RUB",
                },
            },
        },
        {
            "id": 3,
            "description": "Оплата услуг",
            "operationAmount": {
                "amount": "300",
                "currency": {
                    "code": "USD",
                },
            },
        },
    ]


def test_filter_by_currency(transactions: list[dict]) -> None:
    """Проверяет фильтрацию операций по валюте."""
    result = list(filter_by_currency(transactions, "USD"))

    assert len(result) == 2
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"
    assert result[1]["operationAmount"]["currency"]["code"] == "USD"


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """Проверяет получение описаний операций."""
    result = list(transaction_descriptions(transactions))

    assert result == [
        "Перевод организации",
        "Покупка продуктов",
        "Оплата услуг",
    ]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
        ]),
        (10, 11, [
            "0000 0000 0000 0010",
            "0000 0000 0000 0011",
        ]),
    ],
)
def test_card_number_generator(
    start: int, stop: int, expected: list[str]
) -> None:
    """Проверяет генерацию номеров карт."""
    result = list(card_number_generator(start, stop))

    assert result == expected
