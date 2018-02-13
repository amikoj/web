# !/usr/bin/env python
# -*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for
# 导入蓝本 main
from . import main

config = (
    {
        "name": "home",
        "text": "主页",
        "endpoint": "main.index"
    }, 
    {
        "name": "journal",
        "text": "日志",
        "endpoint": "main.journal"
    }, 
    # {
    #     "name": "hobby",
    #     "text": "爱好",
    #     "endpoint": "main.hobby"
    # },
    {
        "name": "blog",
        "text": "博客",
        "endpoint": "main.blog"  
    },
    {
        "name": "share",
        "text": "分享",
        "endpoint": "main.share"
    }
)


@main.route('/')
@main.route('/index')
@main.route('/index.htm')
@main.route('/index.html')
def index():
    return render_template('index.html', config=config)


@main.route('/journal')
@main.route('/journal/')
@main.route('/journal.htm')
@main.route('/journal.html')
def journal():
    return render_template('journal.html', config=config)


@main.route('/hobby')
@main.route('/hobby/')
@main.route('/hobby.htm')
@main.route('/hobby.html')
def hobby():
    return render_template('hobby.html', config=config)


@main.route('/blog')
@main.route('/blog/')
@main.route('/blog.htm')
@main.route('/blog.html')
def blog():
    return render_template('blog.html', config=config)


@main.route('/share')
@main.route('/share/')
@main.route('/share.htm')
@main.route('/share.html')
def share():
    return render_template('share.html', config=config)



