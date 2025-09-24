from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Zeneto</h1>"


@app.route("/sobre")
def sobre():
    return "<p>Esta e a minha rota</p>"
