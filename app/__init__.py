import telebot
from flask import Flask
from config import Config, telegram_API_KEY, socks_port, socks_ip
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
bot = telebot.TeleBot(telegram_API_KEY)
telebot.apihelper.proxy = {'https': f"socks5://{socks_ip}:{socks_port}"}
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

bootstrap = Bootstrap(app)
