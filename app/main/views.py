# !/usr/bin/env python
# -*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for
# 导入蓝本 main
from . import main
# 导入配置参数
from app.main.config import *
context = pageDebugContext


@main.route('/')
def index():
    return render_template('index.html',context=context)


@main.route('/contact.html')
def contact():
    return render_template('contact.html',context=context)

#
# @main.route('/index.html')
# def courseware():
#     return render_template('index.html',context=context)


@main.route('/more.html')
def more():
    return render_template('more.html',context=context)


@main.route('/journal.html')
def journal():
    return render_template('journal.html',context=context)


@main.route('/hobby.html')
def hobby():
    return render_template('hobby.html',context=context)