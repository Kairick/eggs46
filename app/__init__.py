import telebot
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config, telegram_API_KEY

app = Flask(__name__)
bot = telebot.TeleBot(telegram_API_KEY)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

bootstrap = Bootstrap(app)
