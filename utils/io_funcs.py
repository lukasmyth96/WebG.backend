import json
from typing import Union


def read_text_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as text_file:
        data = text_file.read()

    return data


def write_text_file(file_path: str, a_string: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(a_string)


def read_json_file(file_path: str) -> Union[dict, list]:
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    return data


def write_json_file(file_path: str, data: Union[dict, list]) -> None:
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, sort_keys=True, indent=4)
