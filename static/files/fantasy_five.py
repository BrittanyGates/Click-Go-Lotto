import random


def fantasy_five():
    """
    This function binds five variables to random integers. Fantasy 5 doesn't allow for duplicate numbers.
    That is why I created specific ranges for each set of numbers.
    :return: The function returns five numbers to be displayed on the website. They aren't in order to give the
    appearance of randomness.
    """
    num1 = random.randint(1, 7)
    num2 = random.randint(8, 17)
    num3 = random.randint(18, 27)
    num4 = random.randint(28, 37)
    num5 = random.randint(38, 42)
    return num1, num3, num2, num5, num4


fantasy_five()
