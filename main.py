#!/usr/bin/env python3
"""
Title: Lotto Number Generator
Creator: Brittany Gates (https://github.com/brittbot-bgates)
About: This web app randomly generates lottery numbers for the following games:
- Cash 3 / Pick 3
- Cash 4 / Pick 4
- Pick 5
- Fantasy 5
- Mega Millions
- Powerball
"""

from flask import Flask, render_template
from static.files.cash_four import cash_four
from static.files.cash_three import cash_three
from static.files.fantasy_five import fantasy_five
from static.files.mega_millions import mega_millions
from static.files.powerball import powerball

app = Flask(__name__)


@app.route("/")
def index():
    """
    :return: This function loads the index.html page.
    """
    return render_template("index.html")


@app.route("/games/pick3.html", methods=["GET", "POST"])
def cash_three_game():
    """
    :return: This function returns the three random numbers to be displayed on the Cash 3/Pick 3 page.
    """
    num1, num2, num3 = cash_three()
    return render_template("/games/pick3.html", num1=num1, num2=num2, num3=num3)


@app.route("/games/pick4.html", methods=["GET", "POST"])
def cash_four_game():
    """
    :return: This function returns the four random numbers to be displayed on the Cash 4/Pick 4 page.
    """
    num1, num2, num3, num4 = cash_four()
    return render_template("/games/pick4.html", num1=num1, num2=num2, num3=num3, num4=num4)


@app.route("/games/pick5.html", methods=["GET", "POST"])
def pick5_game():
    """
    :return: This function returns the four random numbers to be displayed on the Cash 4/Pick 4 page.
    """
    # num1, num2, num3, num4 = cash_four()
    return render_template("/games/pick5.html", num1=num1, num2=num2, num3=num3, num4=num4)


@app.route("/games/fantasy5.html", methods=["GET", "POST"])
def fantasy_five_game():
    """
    :return: This function returns the five random numbers to be displayed on the Fantasy 5 page.
    """
    num1, num2, num3, num4, num5 = fantasy_five()
    return render_template("/games/fantasy5.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5)


@app.route("/games/mega_millions.html", methods=["GET", "POST"])
def mega_millions_game():
    """
    :return: This function returns the six random numbers to be displayed on the Mega Millions page.
    """
    num1, num2, num3, num4, num5, mega = mega_millions()
    return render_template("/games/mega_millions.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5,
                           mega=mega)


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
