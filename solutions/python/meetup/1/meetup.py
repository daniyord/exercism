import calendar
from datetime import date

calendar.setfirstweekday(calendar.SUNDAY)


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


day_map = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
}


def meetup(year, month, week, day_of_week):
    day = 1

    month_info = calendar.monthcalendar(year, month)

    print(month_info)

    day_of_week_int = day_map[day_of_week]

    match week:
        case "first":
            week_info = month_info[0]
            alternate_week = month_info[1]
        case "second":
            week_info = month_info[1]
        case "third":
            week_info = month_info[2]
        case "fourth":
            week_info = month_info[3]
        case "fifth":
            if len(month_info) < 5:
                raise MeetupDayException("That day does not exist.")
            week_info = month_info[4]
        case "last":
            week_info = month_info[-1]
            alternate_week = month_info[-2]
        # case "teenth":
        #     week_info

    print(week_info)

    day = (
        week_info[day_of_week_int]
        if week_info[day_of_week_int] > 0
        else alternate_week[day_of_week_int]
    )

    return date(year, month, day)


print(meetup(2013, 3, "third", "Sunday"), date(2013, 3, 17))

print(calendar.month(2013, 3))
