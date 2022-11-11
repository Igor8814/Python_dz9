import pyowm
import telebot

bot = telebot.TeleBot("5546915632:AAFqq0aFHKnNNQ2vFJq00YaGlajSwzTe0ic")
owm = pyowm.OWM('198bc5428912d5ba95d5ca90a6f13b3c')
mgr = owm.weather_manager()
@bot.message_handler(content_types=['text'])

def send_echo(message):
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather
    temp = w.get_temperature('celsus')["temp"]

    answer = "В городе" + message.text + "сейчас" + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе" + str(temp) + "\n\n"
    if temp < 10:
        answer += "Сейчас так холодно одевайся теплее!"
    elif temp < 20:
        answer += "Сейчас холодно,одевайся лучше!"
    else:
        answer += "Температура нормальная"
    bot.send_message(message.chat.id, message.text)
bot.infinity_polling(none_stop=True)

