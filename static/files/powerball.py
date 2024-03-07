import random


def powerball():
    """
    Binds six numbers to random integers. Powerball only allows the red Powerball to have a duplicate number 
    (compared to the other five numbers). 
    :return: Returns six random numbers to the games/powerball.html page.
    """
    num1 = random.randint(1, 12)
    num2 = random.randint(13, 24)
    num3 = random.randint(25, 36)
    num4 = random.randint(37, 48)
    num5 = random.randint(49, 69)
    red_powerball = random.randint(1, 26)
    return num1, num2, num3, num4, num5, red_powerball


powerball()
