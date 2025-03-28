from flask import Flask
from app.routes import prefix_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(prefix_blueprint)
    return app
