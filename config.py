import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(verbose=True)


class Config:
    URL = "localhost:" + os.environ.get("FLASK_RUN_PORT") + '/'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
