"""
@author miguelCabrera1001 | 
@date 3/01/20
@project 
@name main.py
"""
import os

import logging
import sys

from flask import Flask, jsonify
from api.utils.database import db
from api.config.config import *
from api.utils.responses import response_with
import api.utils.status_responses as resp
from api.blueprits.author import author_routes

# logging = logging(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(author_routes, url_prefix='/api/authors')

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s | %(levelname)s | %(filename)s | %(lineno)s | %(message)s',
                        level=logging.DEBUG)

    return app


if __name__ == '__main__':
    app.run(port=5000, host="127.0.0.1", use_reloader=False)
