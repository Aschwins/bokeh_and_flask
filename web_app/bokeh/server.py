from web_app.bokeh.app import bkapp
from bokeh.plotting import curdoc

doc = curdoc()

doc = bkapp(doc)
