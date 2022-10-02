from typing import Any


def error_response(data: list[str] | list[dict[str, Any]] | dict[str, Any], non_field: bool = True):
    if non_field:
        return {
            'non_field_errors': list(map(__errDataMap, data))
        }
    else:
        # print({"data": data})
        return data

def __errDataMap(data):
    return data
    # return {"error": data}