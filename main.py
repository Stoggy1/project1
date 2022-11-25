def power(x, y):
    if y == 1:
        return x
    if y != 1:
        return x * power(x, y - 1)


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


def main():
    print("__________Exponential_______")
    print(f"2^3 = {power(2, 3)}")
    print(f"-2^3 = {power(-2, 3)}")
    print(f"1^5 = {power(1, 5)}")
    print("________cat ears____________")
    print(f"0 cats have {cat_ears(0)} ears in total")
    print(f"1 cats have {cat_ears(1)} ears in total")
    print(f"2 cats have {cat_ears(2)} ears in total")
    print("_______alien ears_____________")
    print(f"{alien_ears(1)} ears (alien 1 has 2 ears)")
    print(f"{alien_ears(2)} ears (alien 1 has 2 ears, alien 2 has 3 ears)")

