# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from app import app, bot
from .forms import OrderForm
from .service import *
from config import chat_id


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    if form.validate_on_submit():
        new_order = save_order(form.data)
        bot.send_message(chat_id, new_order)
        return redirect(url_for('done'))
    return render_template('index.html',
                           form=form)


@app.route('/done')
def done():
    return render_template('done.html')


@app.route('/ten', methods=["GET"])
def get_ten():
    order_data = get_ten_orders()
    return order_data


@app.route('/today', methods=["GET"])
def get_today():
    order_data = get_today_orders()
    return order_data


@app.context_processor
def base_processor():
    def get_current_price():
        res = get_price()
        return res

    return dict(get_current_price=get_current_price)
