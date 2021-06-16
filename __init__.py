from apps.models import db
from flask import Flask
from flask_migrate import Migrate
from apps.config import config


def create_app(config_type="STAGING"):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    db.init_app(app)
    migrate = Migrate(app, db)
    # app.wsgi_app = Middleware(app)
    # for exception in default_exceptions:
    #     app.register_error_handler(exception, HandlerError.handler_http_error)

    return app