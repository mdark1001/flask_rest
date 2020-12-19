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
from api.models.author import AuthorSchema, Author
from flask_jwt_extended import jwt_required

author_routes = Blueprint("author_routes", __name__)


@author_routes.route('/', methods=['POST'])
@jwt_required
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        _logger.info(result)
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)


@author_routes.route('/', methods=['GET'])
@jwt_required
def get_authors():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True, only=['id', 'first_name', 'last_name'])
    authors = author_schema.dump(fetched)

    return response_with(resp.SUCCESS_200, value={"authors": authors})


@author_routes.route('/<int:author_id>', methods=['GET'])
@jwt_required
def ger_author_by_id(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    result = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"author": result})
