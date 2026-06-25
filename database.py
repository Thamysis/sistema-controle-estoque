import os

from app import app
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

username = os.environ.get("DB_USERNAME", "root")
password = os.environ.get("DB_PASSWORD", "")
server = os.environ.get("DB_SERVER", "localhost")
database_name = os.environ.get("DB_NAME", "sistemacontroleestoque")


def get_connection():
    database_uri = "mysql://{username}:{password}@{server}/{database}".format(
        username=username,
        password=password,
        server=server,
        database=database_name
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    return SQLAlchemy(app)


database = get_connection()
