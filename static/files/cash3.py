import random


def cash3():
    """
    Binds three numbers to random integers. Cash3 allows for duplicate numbers.
    :return: Returns three random numbers to the games/cash3.html page.
    """
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    return num1, num2, num3


cash3()
