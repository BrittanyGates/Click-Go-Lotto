import random


def cash4():
    """
    Binds four numbers to random integers. Cash4 allows for duplicate numbers.
    :return: Returns three random numbers to the games/cash4.html page.
    """
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    return num1, num2, num3, num4


cash4()
