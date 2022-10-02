from datetime import datetime
from django.utils import timezone


def currentDateTime():
    date_time = datetime.now()
    tz=timezone.get_current_timezone()
    timezone_datetime = timezone.make_aware(value=date_time, timezone=tz, is_dst=True)
    return timezone_datetime

def currentDateTimeOG():
    return datetime.now(tz=timezone.utc)

