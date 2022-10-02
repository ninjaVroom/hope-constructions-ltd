from datetime import datetime


def getDateTime(date: str, format: str):
    return datetime.strptime(date, format)
