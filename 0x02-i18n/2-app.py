#!/usr/bin/env python3
""" A basic Flask app """
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

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """ Simple template rendering """

    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
