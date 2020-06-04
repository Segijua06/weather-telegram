#telegram bot test v2.0
import pyowm
import telebot

owm = pyowm.OWM("849be79a5eba4d090e4fafef41335d89", language = "ru")
bot = telebot.TeleBot("866200603:AAEs8nFqBJHSxjI_ikiwLXVkHrAk6S73lhk")

@bot.message_handler(content_types=["text"])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature("celsius")["temp"]
	speed = w.get_wind()["speed"]
	deg = w.get_wind()["deg"]
	humidity = w.get_humidity() 


	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "🌡 Температура сейчас в районе: " + str(temp) + "  °C " + "\n"
	answer += "💨 Скорость ветра сейчас: " + str(speed) +  " м/с " + "\n"
	answer += "    Направление ветра: " + str(deg) +   "\n"
	answer += "💧 Влажноть: " + str(humidity) + "  % " + "\n\n"



	if temp < 10:
		answer +=  "Сейчас ппц как холодно, одевайся как танк!" 
	elif temp < 20:
		answer +=  "Сейчас холодно, одевайся потеплее." 
	else:
		answer +=  "Температура норм, одевай что угодно." 

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )