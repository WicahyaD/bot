from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', methods=['POST'])
def bot():
    user_msg = request.value.get('Body', '').lower()
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    if 'hi' in user_msg:
        msg.body("""Selamat Datang Di Hallo Indihome, Ada yang bisa saya bantu?
        *Promo* = List promo terbaru
        *Daftar* = Berlangganan indihome
        *Lokasi* = Lokasi plasa bumiayu
        """)
    elif 'Promo' in user_msg:
        msg.body("Promo menarik dapat dilihat disini ,https://indihome.co.id/paket/daftar")
    elif 'Lokasi' in user_msg:
        msg.body("Lokasi plasa bumiayu ,https://goo.gl/maps/TRBLhdJADkkYVwYU6")

    else:
        msg.body("""Selamat Datang Di Hallo Indihome, Ada yang bisa saya bantu?
        *Promo* = List promo terbaru
        *Daftar* = Berlangganan indihome
        *Lokasi* = Lokasi plasa bumiayu
        """)

if __name__ == '__main__':
    app.run()