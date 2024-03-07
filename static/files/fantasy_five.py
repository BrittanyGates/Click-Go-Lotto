import random


def fantasy_five():
    """
    Binds six numbers to random integers. Fantasy Five doesn't allow for duplicate numbers.
    :return: Returns five random numbers to the games/fantasy-five.html page.
    """
    num1 = random.randint(1, 7)
    num2 = random.randint(8, 17)
    num3 = random.randint(18, 27)
    num4 = random.randint(28, 37)
    num5 = random.randint(38, 42)
    return num1, num3, num2, num5, num4


fantasy_five()
