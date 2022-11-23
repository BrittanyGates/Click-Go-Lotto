import random


def cash4_pick4():
    """
    This function binds four numbers to random integers. Cash 4 / Pick 4 allows for duplicate numbers.
    :return: The function returns four numbers to be displayed on the website.
    """
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    return num1, num2, num3, num4


cash4_pick4()
