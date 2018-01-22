# !/usr/bin/env python
# -*-coding:utf-8-*-

from flask_httpauth import HTTPBasicAuth
from .erros import unauthorized,forbidden

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email,password):
    return True


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')
