"""
@author miguelCabrera1001 | 
@date 3/01/20
@project 
@name author
"""
from flask import Blueprint
from flask import request
import logging
from api.utils.responses import response_with
import api.utils.status_responses  as resp
from api.models.author import AuthorSchema

author_routes = Blueprint("author_routes", __name__)


@author_routes.route('/', methods=['POST'])
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create()).data
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)
