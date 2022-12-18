from asgiref.wsgi import WsgiToAsgi

from flask import Flask


app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

import src.api.routers