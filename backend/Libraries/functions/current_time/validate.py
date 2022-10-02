from datetime import datetime


def validateStringDate(date_value: str):
    try:
        return datetime.strptime(date_value, '%Y-%m-%d')
    except ValueError:
        return ValueError(f"'{date_value}' is not a valid date value")


def validateStringTime(time_value: str):
    try:
        return datetime.strptime(time_value, '%H:%M:%S')
    except ValueError:
        return ValueError(f"'{time_value}' is not a valid time value")


def validateStringDateTime(time_value: str):
    try:
        try:
            return datetime.strptime(time_value, '%Y-%m-%dT%H:%M:%S')
        except:
            return datetime.strptime(time_value, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return ValueError(f"'{time_value}' is not a valid date-time value")
