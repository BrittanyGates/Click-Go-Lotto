import random


def mega_millions():
    """
    Binds six numbers to random integers. Mega Millions only allows the Mega Ball to have a duplicate number 
    (compared to the other five numbers). 
    :return: Returns six random numbers to the games/mega-millions.html page.
    """
    num1 = random.randint(1, 13)
    num2 = random.randint(14, 26)
    num3 = random.randint(27, 39)
    num4 = random.randint(40, 52)
    num5 = random.randint(53, 70)
    mega_ball = random.randint(1, 25)
    return num3, num1, num5, num2, num4, mega_ball


mega_millions()
