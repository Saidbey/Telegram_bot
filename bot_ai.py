#In the beginning important libraries should be imported
#Here I have imported libraries for telegram bot and also for connecting bot with OpenCV: numpy, json, face_recognition
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import numpy as np
import json
import face_recognition
admin_id = 1911018009
token = "5320352538:AAG8B14oSb8DeRsNkwzX-UUX1-a8cB8Lnhg"

with open('astrum.json') as json_file:
    data = json.load(json_file)

known_face_encodings = [np.asarray(i['encode']) for i in data]
known_face_data = [f"{i['dir']} -> {i['name']}" for i in data]

def start_com(update, context):
    id = update.message.from_user.first_name
    Id = update.message.from_user.username# I used it in order to know the user's username, started my bot
    update.message.reply_photo(
    photo=open('image/astrum.jpg', 'rb'),
    caption=f"Assalomu aleykum, {id} siz maxsus face_recognition topshirig'i bo'yicha tayyorlangan botga start berdingiz.\nSiz bu botga istalgan shaxsning rasmini yuborasiz va u sizga o'zida bor malumotlarni qaytaradi.",
    )
    context.bot.send_message(chat_id=admin_id, text=f"@{Id} foydalanuvchisi botga start berdi")

def photo_handler(update, context): # This function uploads pic from telegram and gets to our code.
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download('image/photo.jpg')

    uknown_img = face_recognition.load_image_file("image/photo.jpg")
    uknown_encoding = face_recognition.face_encodings(uknown_img)[0] # Here downloaded picture is encoded
    minimum = 0.5
    result_index = None
    for i in range(len(known_face_encodings)):
        face_distances = face_recognition.face_distance([known_face_encodings[i]], uknown_encoding)[0]
        result = face_recognition.compare_faces([known_face_encodings[i]], uknown_encoding)[0]
        print(result,face_distances)
        if result and face_distances < minimum: # Here we used this method to reduce the number of True booleans and to help our program to choose correct one
            minimum = face_distances
            result_index = i

    if result_index != None:
        student_data = f"Astrum o'quvchisi:\nYo'nalishi: \t{data[result_index]['dir']}\nIsm-Familiyasi:   {data[result_index]['name']}".expandtabs(11)
    else:
        student_data = "Topilmadi"
    update.message.reply_text(text=student_data)

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_com))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler ))
    updater.start_polling()
    updater.idle()

main()
