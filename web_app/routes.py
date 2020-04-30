from web_app import app
from flask import render_template, request, make_response

from bokeh.embed import server_document


@app.route('/', methods=['GET'])
def bkapp_page():
    script = server_document('http://localhost:5006/bkapp')
    return render_template("embed.html", script=script, template="Flask")

