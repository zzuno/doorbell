import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'QR Doorbell is alive!'

@app.route('/notify')
def notify():
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')

    if not bot_token or not chat_id:
        return 'Missing credentials', 500

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": "🚪 QR 코드가 스캔되었습니다!"}

    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            return f"Telegram Error {response.status_code}: {response.text}", 500
    except Exception as e:
        return f"Exception during request: {str(e)}", 500

    return '🔔 방문 요청이 접수되었습니다. 잠시만 기다려 주세요.', 200
