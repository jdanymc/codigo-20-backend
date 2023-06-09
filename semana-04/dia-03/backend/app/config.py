from datetime import timedelta
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456.a@localhost/db_shop_g20'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'secret'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)