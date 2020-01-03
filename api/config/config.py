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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mdark1001@localhost:3306/viajes'
    SQLALCHEMY_ECHO = False


class DevelopmentConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mdark1001@localhost:3306/viajes'
    SQLALCHEMY_ECHO = False
