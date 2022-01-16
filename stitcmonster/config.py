import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ""

    @staticmethod
    def init_app(app):
        pass

config = Config()