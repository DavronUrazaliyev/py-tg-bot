from settings import TOKEN
from telegram import Bot
import time

bot = Bot(TOKEN)

last_update_id = -1
while True:
    curr_update = bot.getUpdates()[-1]

    if last_update_id != curr_update.update_id:

        user    = curr_update.message.from_user
        message = curr_update.message

        bot.sendMessage(user.id, message.text)

        last_update_id = curr_update.update_id
    
    time.sleep(0.5)
    