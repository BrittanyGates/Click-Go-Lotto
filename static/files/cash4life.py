import random


def cash4life():
    """
    This function binds six variables to random integers. Cash4Life doesn't allow for duplicate numbers (except for
    the Cash Ball which can be the same number as any of the five numbers). That is why I created specific ranges for
    each set of numbers.
    :return: The function returns six numbers to be displayed on the website.
    """
    num1 = random.randint(1, 13)
    num2 = random.randint(14, 26)
    num3 = random.randint(27, 39)
    num4 = random.randint(40, 52)
    num5 = random.randint(53, 60)
    cash_ball = random.randint(1, 4)
    return num1, num2, num3, num4, num5, cash_ball


cash4life()