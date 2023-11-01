def is_leap(year: int) -> bool:
    return True if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0 else False
