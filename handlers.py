from telegram.ext import CallbackContext
from telegram import Update


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    bot = context.bot

    bot.sendMessage(user.id, 'Asslomu alaykum.')

def echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot

    bot.sendMessage(user.id, message.text)

def echo_photo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot

    bot.sendPhoto(user.id, message.photo[-1])