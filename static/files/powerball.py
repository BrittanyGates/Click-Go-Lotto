import random


def powerball():
    """
    This function binds six variables to random integers. Powerball doesn't allow for duplicate numbers (except for
    the Powerball number which can be the same number as any of the five numbers). That is why I created specific
    ranges for each set of numbers.
    :return: The function returns six numbers to be displayed on the website.
    """
    num1 = random.randint(1, 12)
    num2 = random.randint(13, 24)
    num3 = random.randint(25, 36)
    num4 = random.randint(37, 48)
    num5 = random.randint(49, 69)
    powerball_num = random.randint(1, 26)
    return num1, num2, num3, num4, num5, powerball_num


powerball()
