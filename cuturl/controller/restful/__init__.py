#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask.ext.restful import Api
from cuturl.controller.restful.urlRegistApi import UrlRegistApi

__all__ = ['urlRegistApi']

def initRestfulApi(app):
    api = Api(app)
    api.add_resource(UrlRegistApi, '/api/v1.0/addurl')