#!/usr/bin/env python3
"""A Flask app with Babel configuration, translations, and forced locale"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best language for the user"""
    forced_locale = request.args.get('locale')
    if forced_locale in app.config['LANGUAGES']:
        return forced_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render index.html template with translatable text"""
    return render_template(
            '4-index.html',
            title='Welcome to Holberton',
            header='Hello world'
            )


if __name__ == '__main__':
    app.run()
