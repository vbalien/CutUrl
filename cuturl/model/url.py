#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import current_app
from cuturl.database import db

class Url(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key = True)
    key = db.Column(db.String(current_app.config['KEY_LENGTH']))
    to_url = db.Column(db.String(500))

    def __init__(self, key, to_url):
        self.key = key
        self.to_url = to_url

    def __repr__(self):
        return "<Url('%s', '%s')>" % (self.key, self.to_url)