#!/usr/bin/env python3
"""Bable setup with app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """This class represents a Flask Babel
    configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask('__name__')
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page
    """
    # babel.init_app(app, locale_selector=get_locale)
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """This function method
    returns an index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
