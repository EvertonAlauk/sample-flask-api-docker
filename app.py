from flask import Flask
from flask_restplus import Namespace
from flask_restplus import Resource
from apis import api

app = Flask(__name__)
app.config.from_object('config')
api.init_app(app)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

