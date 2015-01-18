#!/usr/bin/python
# -*- coding: utf-8 -*-
class CuturlConfig(object):
	#: Database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'

    #: URL random key length
    KEY_LENGTH = 10
    #: URL random key letters
    KEY_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'