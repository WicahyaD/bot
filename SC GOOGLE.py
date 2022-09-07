from flask import Flask, request
from googlesearch import search
import requests
import google
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route("/", methods=["POST"]) # rute untuk mengakses bot
def bot():
	# inputan orang
	user_msg = request.values.get('Body', '').lower()
	# objet dari respon
	response = MessagingResponse()
	# perintah pencarian
	q = user_msg + "geeksforgeeks.org"
	# list hasil
	result = []

	# Mencari dan menyimpan hasil
	for i in search(q, tld='co.id', num=3, stop=3, pause=2):
		result.append(i)

	# Menampilkan Hasil
	msg = response.message(f"--- Hasil Pencarian '{user_msg}' Adalah ---")
	msg = response.message(result[0])
	msg = response.message(result[1])
	msg = response.message(result[2])

	return str(response)

if __name__ == "__main__":
	app.run()