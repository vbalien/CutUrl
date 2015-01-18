#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, current_app
from cuturl.controller import *

def create_app(config_filepath = 'config.cfg'):
    app = Flask(__name__)
    from cuturl.cuturl_config import CuturlConfig
    app.config.from_object(CuturlConfig)
    app.config.from_pyfile(config_filepath, silent = True)

    from cuturl.database import DBManager
    DBManager.init(app)

    with app.app_context():
        from cuturl.model import initModels
        initModels()

    DBManager.init_db()

    from cuturl.controller.restful import initRestfulApi
    initRestfulApi(app)
    
    from cuturl.cuturl_blueprint import cuturl
    app.register_blueprint(cuturl)
    return app