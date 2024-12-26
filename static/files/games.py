#!/usr/bin/env python3
import random


def cash3() -> tuple[int, int, int]:
    """This function provides the three numbers for the Cash 3 game.
    The game allows for numbers 0 to 9, and also allows for duplicate numbers.
    :return: Three individual random integers.
    """
    num1: int = random.randint(0, 9)
    num2: int = random.randint(0, 9)
    num3: int = random.randint(0, 9)
    return num1, num2, num3


def cash4() -> tuple[int, int, int, int]:
    """This function provides the four numbers for the Cash 4 game.
    The game allows for numbers 0 to 9, and also allows for duplicate numbers.
    :return: Four individual random integers.
    """
    num1: int = random.randint(0, 9)
    num2: int = random.randint(0, 9)
    num3: int = random.randint(0, 9)
    num4: int = random.randint(0, 9)
    return num1, num2, num3, num4


def cash4life() -> tuple[int, int, int, int, int, int]:
    """This function provides the three numbers for the Cash4Life game.
    The game allows for numbers 1 to 60, but doesn't allow for duplicate numbers except for the Cash Ball.
    :return: Six individual random integers.
    """
    num1: int = random.randint(1, 13)
    num2: int = random.randint(14, 26)
    num3: int = random.randint(27, 39)
    num4: int = random.randint(40, 52)
    num5: int = random.randint(53, 60)
    cash_ball: int = random.randint(1, 4)
    return num1, num2, num3, num4, num5, cash_ball


def fantasy_five() -> tuple[int, int, int, int, int]:
    """This function provides the five numbers for the Fantasy 5 game.
    The game allows for numbers 1 to 42, but doesn't allow for duplicate numbers.
    :return: Five individual random integers.
    """
    num1: int = random.randint(1, 7)
    num2: int = random.randint(8, 17)
    num3: int = random.randint(18, 27)
    num4: int = random.randint(28, 37)
    num5: int = random.randint(38, 42)
    return num1, num3, num2, num5, num4


def mega_millions() -> tuple[int, int, int, int, int, int]:
    """This function provides the six numbers for the Mega Millions game.
    The game allows for numbers 1 to 60, but doesn't allow for duplicate numbers except for the Mega Ball.
    :return: Six individual random integers.
    """
    num1: int = random.randint(1, 13)
    num2: int = random.randint(14, 26)
    num3: int = random.randint(27, 39)
    num4: int = random.randint(40, 52)
    num5: int = random.randint(53, 70)
    mega_ball: int = random.randint(1, 25)
    return num1, num2, num3, num4, num5, mega_ball


def pick3() -> tuple[int, int, int]:
    """his function provides the three numbers for the Pick 3 game.
    The game allows for numbers 0 to 9, and also allows for duplicate numbers.
    :return: Three individual random integers.
    """
    num1: int = random.randint(0, 9)
    num2: int = random.randint(0, 9)
    num3: int = random.randint(0, 9)
    return num1, num2, num3


def pick4() -> tuple[int, int, int, int]:
    """This function provides the four numbers for the Pick 4 game.
    The game allows for numbers 0 to 9, and also allows for duplicate numbers.
    :return: Four individual random integers.
    """
    num1: int = random.randint(0, 9)
    num2: int = random.randint(0, 9)
    num3: int = random.randint(0, 9)
    num4: int = random.randint(0, 9)
    return num1, num2, num3, num4


def pick5() -> tuple[int, int, int, int, int]:
    """This function provides the five numbers for the Pick 5 game.
    The game allows for numbers 0 to 9, and also allows for duplicate numbers.
    :return: Five individual random integers.
    """
    num1: int = random.randint(0, 9)
    num2: int = random.randint(0, 9)
    num3: int = random.randint(0, 9)
    num4: int = random.randint(0, 9)
    num5: int = random.randint(0, 9)
    return num1, num2, num3, num4, num5


def powerball() -> tuple[int, int, int, int, int, int]:
    """This function provides the six numbers for the Powerball game.
    The game allows for numbers 1 to 69, but doesn't allow for duplicate numbers except for the Powerball.
    :return: Six individual random integers.
    """
    num1: int = random.randint(1, 12)
    num2: int = random.randint(13, 24)
    num3: int = random.randint(25, 36)
    num4: int = random.randint(37, 48)
    num5: int = random.randint(49, 69)
    powerball_num = random.randint(1, 26)
    return num1, num2, num3, num4, num5, powerball_num
