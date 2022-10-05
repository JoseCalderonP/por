from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        EMAIL_KEY=os.environ.get('EMAIL_KEY')
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app