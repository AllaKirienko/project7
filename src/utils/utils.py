import json
from pathlib import Path

def read_json_file(file_path: str) -> list[dict]:
    """Читает JSON-файл и возвращает список словарей с данными."""

    try:
        with Path(file_path).open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
