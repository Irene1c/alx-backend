#!/usr/bin/env python3
""" A basic Flask app that implements i18n with flask_babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ app configurations """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# load configuration settings
app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Function that mocks Logging in """

    user_id = request.args.get('login_as')

    if user_id and int(user_id) in users:
        return users[int(user_id)]
    else:
        return None


@app.before_request
def before_request():
    """ function to execute before all other route functions """

    user = get_user()

    if user is not None:
        g.user = user


@babel.localeselector
def get_locale():
    """ Function get user’s preferred locale if it is supported"""

    r_locale = request.args.get('locale')

    # Locale from URL parameters
    if r_locale and r_locale in app.config['LANGUAGES']:
        return r_locale

    # Locale from user settings
    try:
        if g.user and g.user['locale'] in app.config['LANGUAGES']:
            return g.user['locale']
    except AttributeError:
        pass

    # Locale from request header
    h_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if h_locale:
        return h_locale

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def hello():
    """ Simple template rendering """

    return render_template("6-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
