# !/usr/bin/env python
# -*-coding:utf-8-*-
from . import db


class ShareCategory(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),unique =True)
    summary = db.Column(db.Stirng(300))
    icon = db.Column(db.String(100),unique =True)
