дз к 9 семинару
~~~
import requests, json
import telebot

bot = telebot.TeleBot("5546915632:AAFqq0aFHKnNNQ2vFJq00YaGlajSwzTe0ic")
api_key = "198bc5428912d5ba95d5ca90a6f13b3c"

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    global current_temperature
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + str(message.text)
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
    else:
        print(" City Not Found ")
    answer = " Температура (in kelvin unit) = " + str(current_temperature) +"\n Атмосферное давление (in hPa unit) = " + str(current_pressure) +"\n Влажность (in percentage) = " + str(current_humidity) + "\n Описание = " + str(weather_description)
    bot.send_message(message.chat.id, answer)
bot.infinity_polling(none_stop=True)

~~~
