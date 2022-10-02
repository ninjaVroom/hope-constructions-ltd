from typing import Any


def request_data_to_dict(data):
    new_data: dict[str, Any] = {}

    for item in data:
        new_data[item] = data[item]

    return new_data