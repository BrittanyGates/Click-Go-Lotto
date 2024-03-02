import random


def cash3():
    """
    This function binds three numbers to random integers. Cash 3 allows for duplicate numbers.
    :return: The function returns three numbers to be displayed on the website.
    """
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    return num1, num2, num3


cash3()
