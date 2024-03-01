#!/usr/bin/env python3
"""
Title: Lotto Number Generator
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (https://bcgates.com)
About: This web app randomly generates lottery numbers for the following games:
- Cash 3
- Cash 4
- Cash4Life
- Fantasy 5
- Mega Millions
- Pick 3
- Pick 4
- Pick 5
- Powerball
"""

from flask import Flask, render_template
from static.files.cash3 import cash3
from static.files.cash4 import cash4
from static.files.cash4life import cash4life
from static.files.fantasy_five import fantasy_five
from static.files.mega_millions import mega_millions
from static.files.pick3 import pick3
from static.files.pick4 import pick4
from static.files.pick5 import pick5
from static.files.powerball import powerball


app = Flask(__name__)


@app.route("/")
def index():
    """
    :return: This function loads the index.html page.
    """
    return render_template("index.html")

@app.route("/games/cash3.html", methods=["GET", "POST"])
def cash3_game():
    """
    :return: This function returns the three random numbers to be displayed on the Cash 3 page.
    """
    num1, num2, num3 = cash3()
    return render_template("/games/cash3.html", num1=num1, num2=num2, num3=num3)

@app.route("/games/cash4.html", methods=["GET", "POST"])
def cash4_game():
    """
    :return: This function returns the four random numbers to be displayed on the Cash 4 page.
    """
    num1, num2, num3, num4 = cash4()
    return render_template("/games/cash4.html", num1=num1, num2=num2, num3=num3, num4=num4)

@app.route("/games/cash4life.html", methods=["GET", "POST"])
def cash4life_game():
    """
    :return: This function returns the six random numbers to be displayed on the Cash4Life page.
    """
    num1, num2, num3, num4, num5, cash_ball = cash4life()
    return render_template("/games/cash4life.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           cash_ball=cash_ball)

@app.route("/games/fantasy-five.html", methods=["GET", "POST"])
def fantasy_five_game():
    """
    :return: This function returns the five random numbers to be displayed on the Fantasy Five page.
    """
    num1, num2, num3, num4, num5 = fantasy_five()
    return render_template("/games/fantasy-five.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5)

@app.route("/games/mega-millions.html", methods=["GET", "POST"])
def mega_millions_game():
    """
    :return: This function returns the six random numbers to be displayed on the Mega Millions page.
    """
    num1, num2, num3, num4, num5, mega = mega_millions()
    return render_template("/games/mega-millions.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           mega=mega)

@app.route("/games/pick3.html", methods=["GET", "POST"])
def pick3_game():
    """
    :return: This function returns the three random numbers to be displayed on the Pick 3 page.
    """
    num1, num2, num3 = pick3()
    return render_template("/games/pick3.html", num1=num1, num2=num2, num3=num3)

@app.route("/games/pick4.html", methods=["GET", "POST"])
def pick4_game():
    """
    :return: This function returns the four random numbers to be displayed on the Pick 4 page.
    """
    num1, num2, num3, num4 = pick4()
    return render_template("/games/pick4.html", num1=num1, num2=num2, num3=num3, num4=num4)


@app.route("/games/pick5.html", methods=["GET", "POST"])
def pick5_game():
    """
    :return: This function returns the five random numbers to be displayed on the Pick 5 page.
    """
    num1, num2, num3, num4, num5 = pick5()
    return render_template("/games/pick5.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5)

@app.route("/games/powerball.html", methods=["GET", "POST"])
def powerball_game():
    """
    :return: This function returns the six random numbers to be displayed on the Powerball page.
    """
    num1, num2, num3, num4, num5, power_ball = powerball()
    return render_template("/games/powerball.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           power_ball=power_ball)


if __name__ == '__main__':
    index()