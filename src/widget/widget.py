from src.masks.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет"):
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
