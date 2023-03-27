import os
import telebot


bot = telebot.TeleBot("6170513427:AAG_F2nLSV7a3MtupqWcwWgV-S9kpSHScAk")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm maliya Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://drive.google.com/uc?export=download&id=1BJfGsK-2iPf4wfTScjF5zB0qN3k0fZM2")



bot.polling()
