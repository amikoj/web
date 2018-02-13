# !/usr/bin/env python
# -*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for
# 导入蓝本 main
from . import share
from ..models import ShareCategory,Topic


@share.route('/')
@share.route('/index.html')
@share.route('/index')
def index():
    return render_template('share/index.html')


@share.route('/category')
def categorys():
    u"""
    :return:
    """
    return render_template('share/show.html')


@share.route('/category/<name>')
def child_category(name):
    category = ShareCategory.query.filter_by(name =name).first()
    if category is None:
        return render_template('share/no_found.html', name=name)
    return render_template('share/category.html',category = category)


@share.route('/category/<category_name>/<topic_name>')
def topic(category_name,topic_name):
    category = ShareCategory.query.filter(name=category_name).first()
    if category is not None :
        topic = Topic.query.filter(category_id=category.id, name=topic_name)
        if topic is not None:
            return render_template('share/topic.html', category=category, topic=topic)
    return render_template('share/no_found.html')


@share.route('/getlist', methods=['POST'])
def getlist():
    return "{\"status\":101,\"name\":\"hfcai\"}"