#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request, url_for, current_app
from flask.ext.restful import Resource
from cuturl.model.url import Url
from cuturl.database import db
import json
import random
import string
import re

def checkUrl(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return regex.match(url) != None

def random_string(length, letters):
    return ''.join(random.choice(letters) for i in range(length))

class UrlRegistApi(Resource):
    def post(self):
        args = json.loads(request.data.decode('utf-8'))
        to_url = str(args['to_url']).strip()
        if len(to_url) == 0:
            result = {
                u'status' : False,
                u'message' : 'Enter a valid URL'
            }
        else:
            if checkUrl(to_url):
                rnd_key = ''
                is_exist = True
                while is_exist == True:
                    rnd_key = random_string(
                        current_app.config['KEY_LENGTH'],
                        current_app.config['KEY_LETTERS']
                        )
                    is_exist = (db.session.query(Url).filter_by(key = rnd_key).first() != None)
                url = Url(key = rnd_key, to_url = to_url)
                db.session.add(url)
                db.session.commit()
                result = {
                    u'status' : True,
                    u'message' : u'success',
                    u'key' : url.key,
                    u'cuturl' : url_for('cuturl.toUrl', _external=True, key = url.key)
                }
            else:
                result = {
                    u'status' : False,
                    u'message' : 'Not a valid URL format'
                }
        return result