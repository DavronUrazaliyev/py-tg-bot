from telegram.ext import CallbackContext
from telegram import Update
from keyboards import start_keyboard


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    bot = context.bot

    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot

    bot.edit_message_text(bot, 'salon', user.id, message.message_id)
    

def echo_photo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    # message.delete()x
    message.edit_caption(caption='ok')
    # message.reply_photo(message.photo[-1])