from flask import Flask, request
from twilio.rest import Client
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Mensagem recebida:", request.form.to_dict())
    return "OK", 200

@app.route('/')
def home():
    return "Bot Twilio ativo", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
