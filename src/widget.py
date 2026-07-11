from datetime import datetime

from src.masks.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    parts = info.split()

    if len(parts) < 2:
        return "Некорректный ввод"

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет"):
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")
