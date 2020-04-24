# -*- coding: utf-8 -*-

from app import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String, index=True)
    address = db.Column(db.String, index=True)
    phone = db.Column(db.Integer, index=True)
    eggs_count = db.Column(db.Integer, index=True)