#!/usr/bin/env python3
"""Click-Go-Lotto
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: Randomly generates lottery numbers for the multiple popular national and state games.
"""

from flask import Flask, render_template
from static.files.games import cash3, cash4, cash4life, fantasy_five, mega_millions, pick3, pick4, pick5, powerball

app = Flask(__name__)


@app.route("/")
def index() -> render_template:
    """Displays the index.html template.
    :return: Homepage displaying the National and State game buttons.
    """
    return render_template("index.html")


@app.route("/games/cash3.html", methods=["GET", "POST"])
def cash3_game() -> render_template:
    """Displays the cash3.html template.
    :return: Cash 3 page displaying the three random numbers.
    """
    num1, num2, num3 = cash3()
    return render_template("/games/cash3.html", num1=num1, num2=num2, num3=num3)


@app.route("/games/cash4.html", methods=["GET", "POST"])
def cash4_game() -> render_template:
    """Displays the cash4.html template.
    :return: Cash 4 page displaying the four random numbers.
    """
    num1, num2, num3, num4 = cash4()
    return render_template("/games/cash4.html", num1=num1, num2=num2, num3=num3, num4=num4)


@app.route("/games/cash4life.html", methods=["GET", "POST"])
def cash4life_game() -> render_template:
    """Displays the cash4life.html template.
    :return: Cash4Life page displaying the six random numbers.
    """
    num1, num2, num3, num4, num5, cash_ball = cash4life()
    return render_template("/games/cash4life.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           cash_ball=cash_ball)


@app.route("/games/fantasy-five.html", methods=["GET", "POST"])
def fantasy_five_game() -> render_template:
    """Displays the fantasy-five.html template.
    :return: Fantasy Five page displaying the five random numbers.
    """
    num1, num2, num3, num4, num5 = fantasy_five()
    return render_template("/games/fantasy-five.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5)


@app.route("/games/mega-millions.html", methods=["GET", "POST"])
def mega_millions_game() -> render_template:
    """Displays the mega-millions.html template.
    :return: Mega Millions page displaying the six random numbers.
    """
    num1, num2, num3, num4, num5, mega = mega_millions()
    return render_template("/games/mega-millions.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           mega=mega)


@app.route("/games/pick3.html", methods=["GET", "POST"])
def pick3_game() -> render_template:
    """Displays the pick3.html template.
    :return: Pick 3 page displaying the three random numbers.
    """
    num1, num2, num3 = pick3()
    return render_template("/games/pick3.html", num1=num1, num2=num2, num3=num3)


@app.route("/games/pick4.html", methods=["GET", "POST"])
def pick4_game() -> render_template:
    """Displays the pick4.html template.
    :return: Pick 4 page displaying the four random numbers.
    """
    num1, num2, num3, num4 = pick4()
    return render_template("/games/pick4.html", num1=num1, num2=num2, num3=num3, num4=num4)


@app.route("/games/pick5.html", methods=["GET", "POST"])
def pick5_game() -> render_template:
    """Displays the pick5.html template.
    :return: Pick 5 page displaying the five random numbers.
    """
    num1, num2, num3, num4, num5 = pick5()
    return render_template("/games/pick5.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5)


@app.route("/games/powerball.html", methods=["GET", "POST"])
def powerball_game() -> render_template:
    """Displays the powerball.html template.
    :return: Powerball page displaying the six random numbers.
    """
    num1, num2, num3, num4, num5, power_ball = powerball()
    return render_template("/games/powerball.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           power_ball=power_ball)


if __name__ == '__main__':
    index()
