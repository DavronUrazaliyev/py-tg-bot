from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='btn1'), KeyboardButton(text='btn2')
        ],
        [
            KeyboardButton(text='contact', request_contact=True)
        ]
    ]
)
