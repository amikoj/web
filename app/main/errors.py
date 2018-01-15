# !/usr/bin/env python
# -*-encoding:utf-8 -*-
from flask import render_template
from . import main
# 导入配置参数
from app.main.config import context


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html',context=context), 404

