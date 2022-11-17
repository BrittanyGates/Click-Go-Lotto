import random


def mega_millions():
    """
    This function binds six variables to random integers. Mega Millions doesn't allow for duplicate numbers (except for
    the Mega Ball which can be the same number as any of the five numbers). That is why I created specific ranges for
    each set of numbers.
    :return: The function returns six numbers to be displayed on the website.
    """
    num1 = random.randint(1, 13)
    num2 = random.randint(14, 26)
    num3 = random.randint(27, 39)
    num4 = random.randint(40, 52)
    num5 = random.randint(53, 70)
    mega_ball = random.randint(1, 25)
    return num1, num2, num3, num4, num5, mega_ball


mega_millions()
