# !/usr/bin/env python
# -*-encoding:utf-8 -*-
from flask import render_template,session,redirect,url_for
# 导入蓝本 main
from . import main
# 导入配置参数
from app.main.config import context


@main.route('/')
def index():
    return render_template('index.html',context=context)


@main.route('/contact.html')
def contact():
    return render_template('contact.html',context=context)


@main.route('/courseware.html')
def courseware():
    return render_template('courseware.html',context=context)