# !/usr/bin/env python
# -*-coding:utf-8-*-
from . import db
from datetime import datetime


class ShareCategory(db.Model):
    u"""
     分享类别信息
    """
    __tablename__ = "share_category"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    name = db.Column(db.String(50),unique =True)
    summary = db.Column(db.String(300))
    icon = db.Column(db.String(100),unique =True)
    member_since = db.Column(db.DateTime(),default = datetime.utcnow())


class Topic(db.Model):
    u"""
    分享话题,每次分享都是一个话题,话题从属于一个Category.
    """
    __tablename__ = "topics"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(100))
    member_since = db.Column(db.DateTime(),default = datetime.utcnow())

    # 添加外键
    category_id = db.Column(db.Integer,db.ForeignKey('share_category.id'))



