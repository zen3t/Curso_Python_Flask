from flask import Flask

app = Flask(__name__)
from Views import index, contato


if __name__ == "__main__":
    app.run(debug=True)
