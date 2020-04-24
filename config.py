# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

maindb_dict = dict(host='localhost',
                   user='postgres',
                   password='@rbu34eg',
                   database='eggs46',
                   port=5439)

maindb = 'postgresql+psycopg2://{}:{}@{}:{}/{}'\
    .format(maindb_dict["user"], maindb_dict["password"],
            maindb_dict["host"], maindb_dict["port"],
            maindb_dict["database"])

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or "u9i@D0YEqoh~NsF93ApOoYKd"
    SQLALCHEMY_DATABASE_URI = maindb
    SQLALCHEMY_TRACK_MODIFICATIONS = False