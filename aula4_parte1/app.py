import Views
from flask import Flask


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    Views.init_app(app)
    return app
