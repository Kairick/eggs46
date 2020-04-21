# -*- coding: utf-8 -*-"index.html"

from flask import render_template, redirect, url_for
from app import app
from .forms import OrderForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    if form.validate_on_submit():
        return render_template('done.html', form=form)
    return render_template('index.html',
                           form=form)


# @app.route('/done', methods=['GET', 'POST'])
# def done():
#     return render_template("done.html")

