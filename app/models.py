# -*- coding: utf-8 -*-

from app import db
from datetime import datetime
import datetime as dt


class BaseTable(db.Model):
    __abstract__ = True

    '''Уникальный порядковый номер в рамках бд приложения
    '''
    id = db.Column(db.Integer, unique=True, index=True,
                   primary_key=True, nullable=False)
    date_created = db.Column(db.DateTime, index=True,
                             default=dt.datetime.now)
    date_modified = db.Column(db.DateTime, nullable=True,
                              default=dt.datetime.now)
    deleted = db.Column(db.Boolean, nullable=True, default=False)

    def __init__(self, **kwargs):
        self.date_created = datetime.now()


class Order(BaseTable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        BaseTable.__init__(self)
    customer = db.Column(db.String, index=True)
    address = db.Column(db.String, index=True)
    phone = db.Column(db.BIGINT, index=True)
    eggs_count = db.Column(db.Integer, index=True)


class Price(BaseTable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        BaseTable.__init__(self)
    price = db.Column(db.Integer, index=True)