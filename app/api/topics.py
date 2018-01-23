# !/usr/bin/env python
# -*-coding:utf-8-*-

from flask import jsonify,request,g,url_for,current_app
from .. import db
from ..models import ShareCategory,Topic
from . import api
from .erros import forbidden


@api.route('/getCategory')
def get_category():
    u"""
    获取主题信息,可以通过type确定返回为JsonArray还是Json.
    :return:
    """
    # type控制请求类型,type为list返回一个JsonArray,type为single时候返回一个category,此时可以获取一个name属性.
    type = request.args.get('type',"list")
    json  = None
    if type == "list":
        categorys = ShareCategory.query.all()
        return jsonify([category.to_json for category in categorys])
    elif type == "single":
        name = request.args.get('name',"")
        if name is not None and name != "":
            category = ShareCategory.query.filter_by(name = name).first()
            json = category.to_json()
    if json is None:
        json ={
            "status":1000,
            "errorMsg":u"请求参数异常！"
        }
    return jsonify(json)


@api.route('/addCategory',methods = ['POST'])
def add_category():
    json = request.json
    name = json.get("name", None)
    if name is None:
        return jsonify(
            {
                "status": 1000,
                "errorMsg": u"请求参数异常！"
            }
        )

    category = ShareCategory.query.filter_by(name = name).first()
    if category is None:
        category = ShareCategory(name = name)

    category.author = json.get("author", "adm")
    category.summary = json.get('summary','Empty Content.')
    category.icon = json.get('icon',"")
    db.session.add(category)
    db.session.commit()
    return jsonify({
        "status":200,
        "info":category.to_json
    })
