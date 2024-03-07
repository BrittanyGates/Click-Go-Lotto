import random


def pick4():
    """
    Binds four numbers to random integers. Pick4 allows for duplicate numbers.
    :return: Returns four random numbers to the games/pick4.html page.
    """
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    return num1, num2, num3, num4


pick4()
