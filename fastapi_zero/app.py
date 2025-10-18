from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


@app.get('/olamundo', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def ola_mundo():
    return """
      <html>
      <head>
        <title>Exercicio 2!</title>
      </head>
      <body>
        <h1> Welcome to My Website - Page Olá Mundo </h1>
      </body>
    </html>"""
