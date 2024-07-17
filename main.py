import telebot
import qr
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6006716593:AAH4fm80JNBdENzqaovvmyqicyqUPXtBSIs')

VALID_QR_URL = 'http://your-office-url.com/verify'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Пожалуйста, отсканируйте QR-код в заведение, чтобы сделать заказ.")

@bot.message_handler(commands=['menu'])
def send_menu(message):
    bot.send_message(message.chat.id, 'выберите категорию')
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text='салаты', callback_data='salat'))
    menu1.add(telebot.types.InlineKeyboardButton(text='пиццы', callback_data='pizza'))

    if message.text == 'Выбери меня':
        msg = bot.send_message(message.chat.id, text='Нажми первую inline кнопку', reply_markup=menu1)
        bot.register_next_step_handler(msg)

@bot.message_handler(func=lambda message: True)
def handle_qr(message):
    if message.text == VALID_QR_URL:
        bot.send_message(message.chat.id, "QR-код успешно отсканирован. Теперь вы можете сделать заказ.")
    else:
        bot.send_message(message.chat.id, "Неверный QR-код. Попробуйте снова.")

bot.polling()
