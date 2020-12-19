"""
@author miguelCabrera1001 | 
@date 3/01/20
@project 
@name config
"""


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = ''  # IP de produccion


class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:passord@localhost:3306/db'
    SQLALCHEMY_ECHO = False


class DevelopmentConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mdark1001@localhost:3306/homework'
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'f2ea5d2d-df6a-481b-9d33-9063fe644eb4'
    SECURITY_PASSWORD_SALT = '3075e1c9-bdea-424f-8773-9b3852b7c65b'
