# -*- coding: utf-8 -*-
from .models import Order
from app import db


def save_order(data):
    del data['submit']
    del data['csrf_token']
    new_order = Order(**data)
    db.session.add(new_order)
    db.session.commit()



