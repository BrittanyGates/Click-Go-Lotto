import random


def cash4life():
    """
    Binds six numbers to random integers. Cash4Life only allows the Cash Ball to have a duplicate number 
    (compared to the other five numbers). 
    :return: Returns six random numbers to the games/cash4life.html page.
    """
    num1 = random.randint(1, 13)
    num2 = random.randint(14, 26)
    num3 = random.randint(27, 39)
    num4 = random.randint(40, 52)
    num5 = random.randint(53, 60)
    cash_ball = random.randint(1, 4)
    return num1, num3, num5, num2, num4, cash_ball


cash4life()