import random


def pick5():
    """
    Binds five numbers to random integers. Pick5 allows for duplicate numbers.
    :return: Returns five random numbers to the games/pick5.html page.
    """
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    num5 = random.randint(0, 9)
    return num1, num2, num3, num4, num5


pick5()
