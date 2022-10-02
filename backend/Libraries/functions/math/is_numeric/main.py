def maths__isNumeric(number):
    _type = type(number)
    if _type == str or _type == int:
        if _type == str:
            if number.isnumeric() and number.isdigit():
                return True
        else:
            return True
    return False