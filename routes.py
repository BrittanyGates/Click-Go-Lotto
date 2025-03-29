#!/usr/bin/env python3
"""This module contains the routes for the different pages on the website."""
from bs4 import BeautifulSoup
from flask import Blueprint, render_template
from requests import Response
from static.files.games import cash3, cash4, cash4life, fantasy_five, mega_millions, pick3, pick4, pick5, powerball
import requests

routes_bp = Blueprint("routes", __name__)


def get_website_status_codes() -> bool:
    """Determines if the provided URLs return a 200 HTML status code.
    :return: True if all the websites return OK, but False if one fails.
    """
    website_urls: dict[str, str] = {
        "cash4life_url": "https://www.molottery.com/cash4life",
        "mega_millions_url": "https://nclottery.com/mega-millions",
        "powerball_url": "https://www.valottery.com/data/draw-games/powerball",
    }
    response_code: bool = True

    for link in website_urls.values():
        try:
            link_status_code: requests.Response = requests.get(link, timeout=1)
            if link_status_code.status_code != requests.codes.ok:
                response_code = False
        except requests.Timeout:
            return False
        except requests.exceptions.HTTPError:
            return False

    return response_code


def get_cash4life_winning_numbers() -> tuple[str, list[str]] | tuple[str, list[list]]:
    """Gets the latest winning Cash4Life numbers from the Missouri state lottery website.
    :return: Either text of the function's failure, or a tuple containing a header and a list of numbers.
    """
    if get_website_status_codes():
        cash4life_url = "https://www.molottery.com/cash4life"
        cash4life_page = requests.get(cash4life_url, timeout=1)
        soup = BeautifulSoup(cash4life_page.content, "html.parser")
        cash4life_winning_numbers_header = soup.find(class_="game-single-calendar__title").text.strip()
        cash4life_winning_numbers = soup.find_all(class_="game-single-calendar__num")
        cash4life_winning_numbers_list = []

        for numbers in cash4life_winning_numbers:
            cash4life_winning_numbers_list.append(numbers.text.strip())

        return cash4life_winning_numbers_header, cash4life_winning_numbers_list
    else:
        cash4life_winning_numbers_header = "Currently Unavailable"
        cash4life_winning_numbers_list = []

        return cash4life_winning_numbers_header, cash4life_winning_numbers_list


def get_mega_millions_winning_numbers() -> tuple[str, tuple[str, str, str, str, str, str]] | tuple[str, list[list]]:
    """Gets the latest winning Mega Millions numbers from the North Carolina website.
    :return: Either text of the function's failure, or a tuple containing a header and a list of numbers.
    """
    if get_website_status_codes():
        mega_millions_url = "https://nclottery.com/mega-millions"
        mega_millions_page = requests.get(mega_millions_url, timeout=1)
        soup = BeautifulSoup(mega_millions_page.content, "html.parser")
        mega_millions_winning_numbers_header = soup.find(id="ctl00_MainContent_lblDrawdate").text.strip()
        mega_millions_winning_numbers_1 = soup.find(id="ctl00_MainContent_lblNum1").text.strip()
        mega_millions_winning_numbers_2 = soup.find(id="ctl00_MainContent_lblNum2").text.strip()
        mega_millions_winning_numbers_3 = soup.find(id="ctl00_MainContent_lblNum3").text.strip()
        mega_millions_winning_numbers_4 = soup.find(id="ctl00_MainContent_lblNum4").text.strip()
        mega_millions_winning_numbers_5 = soup.find(id="ctl00_MainContent_lblNum5").text.strip()
        mega_millions_winning_numbers_mb = soup.find(id="ctl00_MainContent_lblMegaball").text.strip()
        mega_millions_numbers_list = mega_millions_winning_numbers_1, mega_millions_winning_numbers_2, mega_millions_winning_numbers_3, mega_millions_winning_numbers_4, mega_millions_winning_numbers_5, mega_millions_winning_numbers_mb

        return mega_millions_winning_numbers_header, mega_millions_numbers_list
    else:
        mega_millions_winning_numbers_header = "Currently Unavailable"
        mega_millions_numbers_list = []

        return mega_millions_winning_numbers_header, mega_millions_numbers_list


def get_powerball_winning_numbers() -> tuple[str, list[str]] | tuple[str, list[list]]:
    """Gets the latest winning Powerball numbers from the official website.
    :return: Either text of the function's failure, or a tuple containing a header and a list of numbers.
    """
    if get_website_status_codes():
        powerball_url = "https://www.valottery.com/data/draw-games/powerball"
        powerball_page = requests.get(powerball_url, timeout=1)
        soup = BeautifulSoup(powerball_page.content, "html.parser")
        powerball_winning_numbers_header = soup.find(class_="title-display").text.strip()[:13]
        powerball_winning_numbers = soup.find_all(class_="balls-6")
        powerball_winning_numbers_list = []

        for numbers in powerball_winning_numbers:
            powerball_winning_numbers_list.append(numbers.text.strip()[:2])

        return powerball_winning_numbers_header, powerball_winning_numbers_list
    else:
        powerball_winning_numbers_header = "Currently Unavailable"
        powerball_winning_numbers_list = []

        return powerball_winning_numbers_header, powerball_winning_numbers_list


@routes_bp.route("/")
def index() -> render_template:
    """Displays the index.html template.
    :return: Homepage displaying the National and State game buttons.
    """
    return render_template("index.html")


@routes_bp.route("/games/cash3.html", methods=["GET", "POST"])
def cash3_game() -> render_template:
    """Displays the cash3.html template.
    :return: Cash 3 page displaying the three random numbers.
    """
    num1, num2, num3 = cash3()
    return render_template("/games/cash3.html", num1=num1, num2=num2, num3=num3)


@routes_bp.route("/games/cash4.html", methods=["GET", "POST"])
def cash4_game() -> render_template:
    """Displays the cash4.html template.
    :return: Cash 4 page displaying the four random numbers.
    """
    num1, num2, num3, num4 = cash4()
    return render_template("/games/cash4.html", num1=num1, num2=num2, num3=num3, num4=num4)


@routes_bp.route("/games/cash4life.html", methods=["GET", "POST"])
def cash4life_game() -> render_template:
    """Displays the cash4life.html template.
    :return: Cash4Life page displaying the six random numbers.
    """
    cash4life_header = get_cash4life_winning_numbers()[0]
    cash4life_numbers = get_cash4life_winning_numbers()[1]
    num1, num2, num3, num4, num5, cash_ball = cash4life()
    return render_template("/games/cash4life.html", cash4life_header=cash4life_header,
                           cash4life_numbers=cash4life_numbers, num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           cash_ball=cash_ball)


@routes_bp.route("/games/fantasy-five.html", methods=["GET", "POST"])
def fantasy_five_game() -> render_template:
    """Displays the fantasy-five.html template.
    :return: Fantasy Five page displaying the five random numbers.
    """
    num1, num2, num3, num4, num5 = fantasy_five()
    return render_template("/games/fantasy-five.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5)


@routes_bp.route("/games/mega-millions.html", methods=["GET", "POST"])
def mega_millions_game() -> render_template:
    """Displays the mega-millions.html template.
    :return: Mega Millions page displaying the six random numbers.
    """
    mega_millions_header = get_mega_millions_winning_numbers()[0]
    mega_millions_numbers = get_mega_millions_winning_numbers()[1]
    num1, num2, num3, num4, num5, mega = mega_millions()
    return render_template("/games/mega-millions.html", mega_millions_header=mega_millions_header,
                           mega_millions_numbers=mega_millions_numbers, num1=num1, num2=num2, num3=num3, num4=num4,
                           num5=num5, mega=mega)


@routes_bp.route("/games/pick3.html", methods=["GET", "POST"])
def pick3_game() -> render_template:
    """Displays the pick3.html template.
    :return: Pick 3 page displaying the three random numbers.
    """
    num1, num2, num3 = pick3()
    return render_template("/games/pick3.html", num1=num1, num2=num2, num3=num3)


@routes_bp.route("/games/pick4.html", methods=["GET", "POST"])
def pick4_game() -> render_template:
    """Displays the pick4.html template.
    :return: Pick 4 page displaying the four random numbers.
    """
    num1, num2, num3, num4 = pick4()
    return render_template("/games/pick4.html", num1=num1, num2=num2, num3=num3, num4=num4)


@routes_bp.route("/games/pick5.html", methods=["GET", "POST"])
def pick5_game() -> render_template:
    """Displays the pick5.html template.
    :return: Pick 5 page displaying the five random numbers.
    """
    num1, num2, num3, num4, num5 = pick5()
    return render_template("/games/pick5.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5)


@routes_bp.route("/games/powerball.html", methods=["GET", "POST"])
def powerball_game() -> render_template:
    """Displays the powerball.html template.
    :return: Powerball page displaying the six random numbers.
    """
    powerball_header = get_powerball_winning_numbers()[0]
    powerball_numbers = get_powerball_winning_numbers()[1]
    num1, num2, num3, num4, num5, power_ball = powerball()
    return render_template("/games/powerball.html", powerball_header=powerball_header,
                           powerball_numbers=powerball_numbers, num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           power_ball=power_ball)
