from flask import Flask
from flask_mail import Mail
from .config import Config

mail = Mail()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize Flask-Mail
    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main, url_prefix='/')

    return app

