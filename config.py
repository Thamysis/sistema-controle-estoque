import os

from app import app
from dotenv import load_dotenv

load_dotenv()

# Chave secreta para sessão
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev_secret_key")

# Desabilita eventos do SQL Alchemy (não necessário)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
