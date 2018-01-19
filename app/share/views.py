# !/usr/bin/env python
# -*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for
# 导入蓝本 main
from . import share
from ..models import ShareCategory

# 导入配置参数
from app.main.config import *
context = pageDebugContext


@share.route('/')
@share.route('/index.html')
@share.route('/index.html')
def index():
    return render_template('share/index.html',context = context)


@share.route('/category/<name>')
def category(name):
    category = ShareCategory(name =name)
    return render_template('share/category.html',context =context,category = category)