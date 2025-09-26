"""Extencao flask"""

from flask import request


def init_app(app):
    @app.route("/")
    def index():
        print(request.args)
        print(request.values)
        return "<h1>Ola mundo</h1>"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"
