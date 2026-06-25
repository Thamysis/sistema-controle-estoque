from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
_csrf = CSRFProtect(app)

# Configurações de Módulos
import config

# Views
import views.usuario
import views.produto

if __name__ == '__main__':
    app.run()
