#!/usr/bin/python
# -*- coding: utf-8 -*-
from cuturl import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)