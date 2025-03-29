#!/usr/bin/env python3
"""Click-Go-Lotto
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: Randomly generates lottery numbers for the multiple popular national and state games.
"""
from flask import Flask
from routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run()
