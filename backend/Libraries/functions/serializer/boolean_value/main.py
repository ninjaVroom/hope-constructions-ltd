from typing import Any


            # if isRecuring is not None:
            #     # print({"isRecuring": isRecuring})
            #     boolStr = str(isRecuring).lower()
            #     isRecuring = True if boolStr == 'on' else False
            #     isRecuring = True if boolStr == '1' else isRecuring
            #     isRecuring = True if boolStr == 'true' else isRecuring
            # else:
            #     isRecuring = False
def boolean_field_value(value: Any):
    if value is not None:
        # print({"value": value})
        boolStr = str(value).lower()
        new_value: bool = True if boolStr == 'on' else False
        new_value = True if boolStr == '1' else new_value
        new_value = True if boolStr == 'true' else new_value
    else:
        new_value: bool = False
    return new_value
