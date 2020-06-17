# -*- coding: utf-8 -*-

from app import bot
from app.service import *
from config import chat_id


@bot.message_handler(commands=['last', 'ten', 'today'])
def send_order(message):
    if message.text == '/last':
        msg = get_last_order()
    if message.text == '/today':
        msg = get_today_orders()
    if message.text == '/ten':
        msg = get_ten_orders()
    msg = create_answer(msg)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands='цена')
def set_new_price(message):
    set_price(message)
    bot.send_message(chat_id, "Новая цена установлена")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
