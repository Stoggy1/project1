def power(value_x: float, exponent_y: float) -> float:
    """
    This function calculates the power of a number. It takes in a value and an
exponent, and returns the result
     If the exponent is 1, it returns the value itself. If the exponent is not 1,
it calculates the power by multiplying the value with the result of the
    power function called with the value and exponent - 1. If the result is
greater than 999999999999, a
    RuntimeWarning is raised.
    """
    if exponent_y == 1:
        return value_x
    if exponent_y != 1:
        expo = value_x * power(value_x, exponent_y - 1)
        if expo > 999999999999:
            raise RuntimeWarning
        return expo


def cat_ears(n: int) -> int:
    """
    This function calculates the total number of cat ears based on the number of
cats. It takes n representing the number of cats, and returns the total number of cat ears.

    If the number of cats is 0, it returns 0. Otherwise, it calculates the total number of ears recursively by
adding 2 to the result of the cat_ears function called with n - 1.
    """
    if n == 0:
        return 0
    else:
        return 2 + cat_ears(n - 1)


def alien_ears(n: int) -> int:
    """
    This function calculates the total number of alien ears based on the number
of aliens. It takes n representing the number of aliens, and returns the total number of alien
ears.
    If the number of aliens is 0, it returns 0. If the number of aliens is even, it calculates the total
number of ears recursively by adding 3 to the result of the alien_ears function called with n - 1.

    If the number of aliens is odd, it calculates the total number of ears recursively by
adding 2 to the result of the alien_ears function called with n - 1.
    """
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 3 + alien_ears(n - 1)
    else:
        return 2 + alien_ears(n - 1)
