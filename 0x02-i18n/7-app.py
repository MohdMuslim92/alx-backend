#!/usr/bin/env python3
"""A Flask app with Babel configuration, translations, and user
authentication"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Retrieve user information"""
    return users.get(int(user_id))


app.before_request


@app.before_request
def before_request():
    """Handle user authentication before processing requests"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None


@babel.localeselector
def get_locale():
    """Determine the best language for the user"""
    # Check for locale from URL parameters
    forced_locale = request.args.get('locale')
    if forced_locale in app.config['LANGUAGES']:
        return forced_locale

    # Check for locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Check for locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determine the best time zone for the user"""
    # Check for timezone from URL parameters
    requested_timezone = request.args.get('timezone')
    if requested_timezone:
        try:
            # Validate if the timezone is valid
            pytz.timezone(requested_timezone)
            return requested_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check for timezone from user settings
    if g.user and g.user['timezone']:
        try:
            # Validate if the timezone is valid
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return 'UTC'  # Default to UTC if no valid timezone found


@app.route('/')
def index():
    """Render index.html template with user status"""
    user_status = _('not_logged_in')
    if g.user:
        user_status = _('logged_in_as') % {'username': g.user['name']}
    return render_template(
            '5-index.html',
            title=_('home_title'),
            header=_('home_header'),
            user_status=user_status
            )


if __name__ == '__main__':
    app.run()
