# -*- coding: UTF-8 -*-
import json

from flask import Flask

from blueprints.auth import bp as auth_app
app = Flask(__name__)

app.register_blueprint(auth_app)


if __name__ == '__main__':
    app.run()
