from flask_bootstrap import Bootstrap5
from .main import bp

def init_app(app):
    app.register_blueprint(bp)
    bootstrap = Bootstrap5(app)