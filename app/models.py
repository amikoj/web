# !/usr/bin/env python
# -*-coding:utf-8-*-
from . import db
from datetime import datetime
from flask import url_for,current_app
from app.exceptions import ValidationError


class ShareCategory(db.Model):
    u"""
     分享类别信息
    """
    __tablename__ = "share_category"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    name = db.Column(db.String(50),unique =True)
    author = db.Column(db.String(50))
    summary = db.Column(db.String(300))
    icon = db.Column(db.String(100),unique =True)
    member_since = db.Column(db.DateTime(),default = datetime.utcnow())

    def to_json(self):
        json_category = {
            'auth':self.author,
            'name':self.name,
            'summary':self.summary,
            'icon':self.icon,
            'member_since':self.member_since,
            'url':url_for('share.child_category',name = self.name)
        }
        return json_category

    @staticmethod
    def from_json(json_category):
        name = json_category.get('name')
        if name is None or name == '':
            raise ValidationError('Category does not have a name.')
        return ShareCategory(name = name)


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



