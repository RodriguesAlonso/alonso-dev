from flask import Flask
from alonso_dev.ext import site

def create_app():
    app = Flask(__name__)
    site.init_app(app)
    return app



#if __name__ == '__main__':
#   app.run()
    