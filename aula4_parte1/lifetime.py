# Contexto
from logging import debug
from flask import Flask, request, session

app = Flask(__name__)
## 1 Configuracao
## Add configuração
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB_URI"] = "mysql://...."

## Registrar rotas

@app.route("/path")
def funcao():
    ...
app.add_url_rule("path",callable)

## Inicializar extencao
from flask import Admin
Admin.init_app(app)

## Registrar Blueprints
app.register_blueprint(....)

## Add hooks
@app.before_request(...)
@app.error_handler(...)

## Chamar outras factorieso
views.init_app(app)

## 2 App Context

### App está pronto 'App'

### Testar
# app.test_client
# debug
# objestos globais do Flask
# (request,session,g)
# - Hooks

from flask import  current_app
## Request Context
# Usar os globais do flask
from flask import request,session,g
request.args
request.form
