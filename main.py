# Library's used in bot . 
import requests
import telebot
import validators

# Secret's of User 
username = "***********"
password = "***********"
API_TOKEN = '1234567:AAFDSGDFHFGJHFHGJ6567U6Q'

# Error code
codes = {201 : "This URL has been successfully added to this Instapaper account.",
	 400 : "Bad request or exceeded the rate limit",
	 403 : "Invalid username or password",
	 500 : "The service encountered an error . Please try again later . "}

# Function for link validation and submition of link . 
def instapaper(message):
	if message.from_user.id ==  964149110:
		if validators.url(message.text):
			r = requests.post("https://www.instapaper.com/api/add",
			data={"username" : username , "password" :password , "url": message.text} )
			return codes[r.status_code]
		else:
			return "Provide a valid link"
	else:
		return "Not authorised to use the bot ."

bot = telebot.TeleBot(API_TOKEN)
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there,
This instapaper bot is personal use of @iamxenium only 
Deploy your own from github.com/xeniumcode/instapaper .\
    """)

# Connection between telegram and instapaper function . 
@bot.message_handler(func=lambda message: True)
def echo_message(message):
	bot.reply_to(message, instapaper(message))


bot.infinity_polling()
