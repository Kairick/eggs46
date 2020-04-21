# -*- coding: utf-8 -*-

import phonenumbers
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired


def validate_phone(field):
    if field is not None:
        if len(str(field)) > 16:
            raise ValidationError('Указан некорректный номер телефона')
        try:
            input_number = phonenumbers.parse(field)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Указан некорректный номер телефона')
        except:
            input_number = phonenumbers.parse("+7" + field)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Указан некорректный номер телефона')


class OrderForm(FlaskForm):
    customer = StringField("Имя заказчика", validators=[DataRequired()])
    address = StringField('Адрес доставки', validators=[DataRequired()])
    phone = IntegerField('Контактный номер телефона', validators=[DataRequired()])
    eggs_count = IntegerField('Количество коробов', validators=[DataRequired()])
    submit = SubmitField('Сделать заказ')
