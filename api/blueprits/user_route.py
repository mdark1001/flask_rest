"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 25/09/20
@project 
@name user_route

"""

from flask import Blueprint
from flask import request
import logging
from api.utils.responses import response_with
import api.utils.status_responses  as resp
from api.models.user import User, UserSchema
from flask_jwt_extended import create_access_token
from api.utils.token import confirm_verification_token, generate_verification

from api.utils.database import db

user_routes = Blueprint("user_routes", __name__)


@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        data['password'] = User.generate_hash(data['password'])
        user_schema = UserSchema()
        user = user_schema.load(data)
        result = user_schema.dump(user.create())
        return response_with(resp.SUCCESS_201, value={"user": result})

    except Exception as e:
        logging.error(e)
        return response_with(resp.INVALID_INPUT_422)


@user_routes.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        logging.error(request.get_json())
        current_user = False
        if data.get('email',False):
            current_user = User.find_by_email(data['email'])
        elif data.get('username',False):
            current_user = User.find_by_username(data['username'])

        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if current_user and not current_user.is_verified:
            return response_with(resp.BAD_REQUEST_400)

        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            return response_with(resp.SUCCESS_200, value={
                'message': 'Logged in as {}'.format(current_user.username),
                "access_token": access_token,
            })
        else:
            return response_with(resp.UNAUTHORIZED_403)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@user_routes.route('/confirm/<token>', methods=['GET'])
def verify_token(token):
    try:
        email = confirm_verification_token(token)
        user = User.query.filter_by(email=email).first_or_404()
        if user.is_verified:
            return response_with(resp.INVALID_INPUT_422)
        else:
            user.is_verified = True
            db.session.add(user)
            db.session.commit()
            return response_with(resp.SUCCESS_200,
                                 value={'message': "E-mail virifired, you can proceed to login now"})
    except Exception as ee:
        return response_with(resp.SERVER_ERROR_500)
