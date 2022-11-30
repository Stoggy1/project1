
def power(value_x, exponent_y):
    if exponent_y == 1:
        return value_x
    if exponent_y != 1:
        return value_x * power(value_x, exponent_y - 1)


def cat_ears(n):
    if n == 0:
        return 0
    else:
        return 2 + cat_ears(n - 1)


def alien_ears(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 3 + alien_ears(n - 1)
    else:
        return 2 + alien_ears(n - 1)




