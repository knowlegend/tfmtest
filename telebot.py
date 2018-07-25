import telebot
#import cv2
import time

bot = telebot.TeleBot("579089832:AAFcH3QPjgtVfzPuc-2563hMiMN_izI7aLA")

@bot.message_handler(commands=['start'])
def start_command(message):
   bot.send_message(
       message.chat.id,
       'Greetings! I can convert color images to grayscale images\n' +
       'To get started send a color image to me.\n' +
       'To get help press /help.'
   )

@bot.message_handler(commands=['help'])
def help_command(message):
   bot.send_message(
       message.chat.id,
       'Send a color image to me !'
   )

@bot.message_handler(content_types=['text'])
def text_msg(message):
	bot.send_message(
       message.chat.id,
       'I am trained only to work on images ,type /help for more info'
   )



#@bot.message_handler(content_types=['photo'])
#def photo(message):
#    bot.reply_to(message, "Image received!")
#    print('message.photo =', message.photo)
#    fileID = message.photo[-1].file_id
#    print('fileID =', fileID)
#    file_info = bot.get_file(fileID)
#    print ('file.file_path =', file_info.file_path)
#    downloaded_file = bot.download_file(file_info.file_path)
#    bot.send_message(message.chat.id,'Processing...')
#    with open('image.jpg', 'wb') as new_file:
#        new_file.write(downloaded_file)
#    image = cv2.imread('image.jpg')
#    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    cv2.imwrite('gray_image.jpg',gray_image)
#    file_data = open('gray_image.jpg', 'rb')
#    bot.send_photo(message.chat.id,file_data)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
