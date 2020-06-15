# -*- coding: utf-8 -*-
import json
from .models import Order, Price
from app import db
from .common import mapping


def save_order(data):
    """Save order to base"""
    del data['submit']
    del data['csrf_token']
    new_order = Order()
    new_order.customer = data['customer']
    new_order.address = data['address']
    new_order.phone = data['phone']
    new_order.eggs_count = data['eggs_count']
    db.session.add(new_order)
    db.session.commit()
    answer = json.loads(get_last_order())
    answer = create_answer([answer])
    return answer


def get_last_order():
    """Get last order"""
    order = Order.query.order_by(Order.id.desc()).first()
    order_dict = mapping.single_object_map(order)
    order_dict = mapping.convert_date(order_dict)
    return order_dict


def get_ten_orders():
    """Get last ten orders"""
    order = Order.query.order_by(Order.id.desc()).limit(10).all()
    order_dict = mapping.map_sql_objects_fields(order)
    order_dict = mapping.convert_date(order_dict)
    return json.dumps(order_dict)


def get_today_orders():
    """Get today orders"""
    order = Order.query.order_by(Order.id.desc()).limit(10).all()
    order_dict = mapping.map_sql_objects_fields(order)
    order_dict = mapping.convert_date(order_dict)
    return json.dumps(order_dict)


def get_price():
    """Get current price"""
    price = Price.query.first()
    return price.price


def set_price(new_price):
    """Set new price"""
    price = Price.query.first()
    raw_price = new_price.text.split(' ')[-1]
    price.price = raw_price
    db.session.commit()


def create_answer(orders):
    """Create answer for Bot"""
    answer = ''
    for order in orders:
        answer += f'Заказ номер {order["id"]}\n'
        answer += f'Заказчик - {order["customer"]}\n'
        answer += f'Адрес - {order["address"]}\n'
        answer += f'Телефон -  {order["phone"]}\n'
        answer += f'Количество коробов - {order["eggs_count"]}\n'
        answer += '------------------------------------------\n'
    return answer