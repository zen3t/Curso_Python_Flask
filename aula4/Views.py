"""Extencao flask"""


def init_app(app):
    @app.route("/")
    def index():
        return "<h1>Ola mundo</h1>"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"
