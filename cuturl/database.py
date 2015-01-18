#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy

db = None

class DBManager:
    """DataBase Manager Class"""

    @staticmethod
    def init(app):
        global db
        db = SQLAlchemy(app)

    @staticmethod
    def init_db():
        global db
        db.create_all()

    @staticmethod
    def clear_db():
        global db
        db.drop_all()