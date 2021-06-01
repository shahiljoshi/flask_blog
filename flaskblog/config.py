import os

class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get('EMAIL_USER')
        MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        GOOGLE_CLIENT_ID = "714941756765-pqgsjlv2g0b8qd9bmnlc09s4jgiejn5l.apps.googleusercontent.com"
        GOOGLE_CLIENT_SECRET = "4_GJcHiYsahL73KFc6Q12agt"
        GITHUB_CLIENT_ID = "7ea8941cf78bef72ee2c"
        GITHUB_CLIENT_SECRET = "bf850fe7303c5d0fc7fdc446ce9f01379cbcc7cc"



# obj = Config()
# print(obj.SECRET_KEY)