from web_app import app
from web_app.bokeh.app import bkapp
from flask import render_template, request, make_response

from bokeh.embed import server_document
from tornado.ioloop import IOLoop
from threading import Thread
from bokeh.server.server import Server


# Bokeh Server
def bk_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/bkapp': bkapp}, io_loop=IOLoop(), allow_websocket_origin=["localhost:8000"])
    server.start()
    server.io_loop.start()


Thread(target=bk_worker).start()


@app.route('/', methods=['GET'])
def bkapp_page():
    script = server_document('http://localhost:5006/bkapp')
    return render_template("embed.html", script=script, template="Flask")

