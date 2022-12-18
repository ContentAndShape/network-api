from asgiref.wsgi import WsgiToAsgi

from flask import Flask

from src.core.events import startup


def create_app() -> Flask:
    app = Flask(__name__)
    startup(app=app)

    return app


app = create_app()
asgi_app = WsgiToAsgi(app)

from src.api.routers import (
    users,
    posts,
    comments,
)