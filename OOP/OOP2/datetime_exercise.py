from datetime import date, datetime


def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # print(today)
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    if today.month > birthday.month:
        next_birthday = datetime(today.year+1, birthday.month,birthday.day)
    days = next_birthday - today
    return days
birthday = datetime(2001, 10, 21)
print(days_until_birthday(birthday))


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
# not working: AttributeError: attribute 'day' of 'datetime.date' objects is not writable
    # x = b1 - b2
    # if b1 - b2 != 2*x:
    #     b1.day = b1.day+1
    #     b2.day = b2.day+1
    # else:
    #     return b1
    assert b1 > b2
    delta = b1 - b2
    dday = b1 + delta
    return dday
# TODO Why this is the day that b1 is double d2?

def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1999, 10, 29)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2017, 12, 25)
    b2 = datetime(2010, 11, 1)
    # print(b1-b2)
    print('Double Day', end=' ')
    print(double_day(b1, b2))




if __name__ == '__main__':
    datetime_exercises()
