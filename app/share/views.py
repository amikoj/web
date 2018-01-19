# !/usr/bin/env python
# -*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for
# 导入蓝本 main
from . import share
from ..models import ShareCategory,Topic

# 导入配置参数
from app.main.config import *
context = pageDebugContext


@share.route('/')
@share.route('/index.html')
@share.route('/index')
def index():
    return render_template('share/index.html',context = context)


@share.route('/category')
def categorys():
    u"""
    :return:
    """
    return render_template('share/show.html', context=context)


@share.route('/category/<name>')
def child_category(name):
    category = ShareCategory.query.filter(name =name).first()
    if category is None:
        return render_template('share/category.html',context=context)
    return render_template('share/category.html',context =context,category = category)


@share.route('/category/<category_name>/<topic_name>')
def topic(category_name,topic_name):
    category = ShareCategory.query.filter(name = category_name).first()
    if category is not None :
        topic = Topic.query.filter(category_id = category.id ,name = topic_name)
        if topic is not None:
            return render_template('share/topic.html', context=context,category = category,topic = topic)
    return render_template('share/no_found.html',context=context)

