#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request, redirect, render_template
from cuturl.cuturl_blueprint import cuturl

@cuturl.route("/")
def page_index():
    return render_template('layout.html')

@cuturl.route("/<key>")
def toUrl(key):
    from cuturl.database import db
    from cuturl.model.url import Url
    url = db.session.query(Url).filter_by(key = key).first()
    if url == None:
    	return ''
    else:
        return redirect(url.to_url)