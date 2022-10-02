from datetime import datetime
from typing import Any

from Libraries.classes.code_execution_timer.main import CodeExecutionTimer


CET = CodeExecutionTimer()

def object_is_list_of_strings(data_object: Any):
    CET.starttime()
    is_list_of_strings = True
    if type(data_object) is list:
        for item in data_object:
            if type(item) is not str:
                is_list_of_strings = False

    else:
        is_list_of_strings = False

    CET.endtime()
    CET.printExecTime

    return is_list_of_strings


def object_is_list_of_strings_alt(data_object: Any):
    CET.starttime()
    is_list_of_strings = (True if type(item) is str else False for item in data_object) if (
        type(data_object) is list) else False
    CET.endtime()
    CET.printExecTime
    return bool(is_list_of_strings)
