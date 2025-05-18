from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
login_manager: LoginManager = LoginManager()


def create_app() -> Flask:
    from app.routes import bp as bp_app
    from settings import settings

    app = Flask(__name__)

    app.config.update(**settings.__dict__)

    csrf.init_app(app)

    app.register_blueprint(bp_app, url_prefix="/")

    return app
