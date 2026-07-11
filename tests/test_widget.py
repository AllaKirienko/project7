import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info, expected",
    [
        (
            "Visa Platinum 7000792289606361",
            "Visa Platinum 7000 79** **** 6361",
        ),
        (
            "Счет 73654108430135874305",
            "Счет **4305",
        ),
    ],
)
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected


def test_mask_account_card_empty():
    assert mask_account_card("") == "Некорректный ввод"


def test_mask_account_card_without_number():
    assert mask_account_card("Счет") == "Некорректный ввод"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
