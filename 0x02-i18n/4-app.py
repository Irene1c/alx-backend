#!/usr/bin/env python3
""" A basic Flask app that implements i18n with flask_babel"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """ Function get locale from request """

    r_locale = request.args.get('locale')

    if r_locale and r_locale in app.config['LANGUAGES']:
        return r_locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """ Simple template rendering """

    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
