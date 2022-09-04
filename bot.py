import streamlit as st
from telebot import *
import pafy
import os

st.write("Hai...")

api = "5451328552:AAHQrBiYiiDNJgfwjpdm9c_eK3FraKUZinA"
bot = TeleBot(api)

@bot.message_handler(commands=["mp4"])

def video(message):
    bot.send_message(message.chat.id, "On Progressing...")
    url = pafy.new(message.text.replace("/mp4", ""))
    bot.send_message(message.chat.id, url.title)
    bot.send_message(message.chat.id, "Please Wait...")
    hasil = url.getbest()
    hasil.download()

    for i in os.listdir():
        if i.endswith(".mp4"):
            print(i)
            bot.send_message(message.chat.id, open(i, "rb"))
            os.remove(i)

bot.polling()
