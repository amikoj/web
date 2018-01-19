# !/usr/bin/env python
# -*-coding:utf-8-*-
from . import db
from datetime import datetime

class ShareCategory(db.Model):
    u"""
     分享类别信息
    """
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),unique =True)
    summary = db.Column(db.String(300))
    icon = db.Column(db.String(100),unique =True)
    member_since = db.Column(db.DateTime(),default = datetime.utcnow())



class ShareTopic(db.Model):
    u"""
    分享话题
    """
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),unique =True)
