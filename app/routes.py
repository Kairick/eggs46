# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from app import app
from .forms import OrderForm
from .service import save_order


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    if form.validate_on_submit():
        save_order(form.data)
        return render_template('done.html', form=form)
    return render_template('index.html',
                           form=form)


