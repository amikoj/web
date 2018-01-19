# !/usr/bin/env python
# -*-coding:utf-8-*-
from flask import render_template,url_for
from . import main
from app.main.config import *
context = pageContext


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html',context=context), 404

