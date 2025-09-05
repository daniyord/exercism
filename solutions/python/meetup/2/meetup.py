import calendar
from datetime import date


class MeetupDayException(ValueError):
    def __init__(self, message):
        self.message = message


WEEKDAYS = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

START_DAYS = {
    "first": 1,
    "second": 8,
    "third": 15,
    "fourth": 22,
    "fifth": 29,
    "teenth": 13,
    "last": None,
}


def meetup(year, month, week, day_of_week):
    days_in_month = calendar.monthrange(year, month)[1]
    wanted_week_start = START_DAYS[week] or days_in_month - 6

    if wanted_week_start > days_in_month:
        raise MeetupDayException("That day does not exist.")

    week_day = calendar.weekday(year, month, wanted_week_start)

    delta = (WEEKDAYS[day_of_week] - week_day) % 7

    day = wanted_week_start + delta

    if day > days_in_month:
        raise MeetupDayException("That day does not exist.")

    return date(year, month, day)
