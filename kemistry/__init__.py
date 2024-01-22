from flask import Flask


def create_app():
    """
    Create and return an app instance of Flask.
    """
    app = Flask(__name__)

    return app
