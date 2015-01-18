#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint
cuturl = Blueprint('cuturl', __name__,
                        template_folder = 'templates',
                        static_url_path = '/static',
                        static_folder = 'static')