#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from spider import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))

    def __init__(self,nickname,password):
        self.nickname = nickname
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class DataSets(db.Model):
    __tablename__ = 'datasets'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64))
    body = db.Column(db.Text)
    resource_id = db.Column(db.Integer)

    def __init__(self,label,body,resource_id):
        self.label = label
        self.body = body
        self.resource_id = resource_id

    def __repr__(self):
        return '<Label %r>' % (self.label)