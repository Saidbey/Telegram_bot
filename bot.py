from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
admin_id = 1911018009
def start_command(update, context):
    # print(update.message.text)
    # print(context.bot)
    # print(update.message.from_user.id)
    # update.message.reply_text("/start command has been submitted")
    context.bot.send_message(chat_id="1911018009", text="You have submitted new /start command")

def show_menu(update, context):
    buttons = [
        [KeyboardButton(text="Send Contact", request_contact=True),
         KeyboardButton(text="Send Location", request_location=True)],
        [KeyboardButton(text="Menu3"), KeyboardButton(text="Menu4")]
    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )

def message_handler(update, context):
    Id = update.message.from_user.id
    message = update.message.text
    update.message.reply_text(text=f"You have send '{message}'")
    context.bot.send_message(chat_id=admin_id, text=f"{Id} sent you '{message}'")

def contact_handler(update, context):
    phone_num = update.message.contact.phone_number
    update.message.reply_text(text=f"Your phone number: +{phone_num}")
    context.bot.send_message(chat_id=admin_id, text=f"You have recieved new phone number: +{phone_num}")

def location_handler(update, context):
    Id2 = update.message.from_user.username
    location = update.message.location
    # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
    context.bot.send_location(chat_id=admin_id, latitude=location.latitude, longitude=location.longitude,)
    context.bot.send_message(chat_id=admin_id, text=f"@{Id2} Sizga o'z lokatsiyasini yubordi")

def main():
    updater = Updater(token="5320352538:AAG8B14oSb8DeRsNkwzX-UUX1-a8cB8Lnhg")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text,message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()