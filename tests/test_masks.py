import pytest

from src.masks.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_get_mask_account():
    assert get_mask_account("1234567890123456") == "**3456"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1111222233334444", "1111 22** **** 4444"),
        ("9999888877776666", "9999 88** **** 6666"),
    ],
)
def test_card_mask_multiple(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_card_number_wrong_length():
    with pytest.raises(ValueError):
        get_mask_card_number("123")


def test_account_wrong_length():
    with pytest.raises(ValueError):
        get_mask_account("12")