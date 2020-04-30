from flask import Flask

from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from tornado.ioloop import IOLoop
from threading import Thread
from bokeh.server.server import Server
from web_app.bokeh.app import bkapp

load_dotenv(verbose=True)

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from web_app import routes, models


# Bokeh Server
def bk_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/bkapp': bkapp}, io_loop=IOLoop(), allow_websocket_origin=["localhost:8000"])
    server.start()
    server.io_loop.start()


Thread(target=bk_worker).start()

