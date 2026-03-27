def leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    if year % 4 == 0:
        return True
    return False