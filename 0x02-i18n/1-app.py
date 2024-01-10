#!/usr/bin/env python3
"""A Flask app with Babel configuration"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """Render index.html template"""
    return render_template(
            '1-index.html',
            title='Welcome to Holberton',
            header='Hello world'
            )


if __name__ == '__main__':
    app.run()
