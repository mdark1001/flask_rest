"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 28/09/20
@project 
@name token

"""
from itsdangerous import URLSafeTimedSerializer
from flask import current_app


def generate_verification(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(
        email, salt=current_app.config['SECURITY_PASSWORD_SALT']
    )


def confirm_verification_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except Exception as e:
        return e
    return email
