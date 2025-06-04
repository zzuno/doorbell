import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'QR Doorbell is alive!'

@app.route('/notify')
def notify():
    bot_token = '8180049901:AAEZNdg0kRRR-Mm-INlOd3faFQCGOo4nD7Y'
    chat_id = '6207359753'
    text = '🚪 QR 코드가 스캔되었습니다! 누군가 초인종을 눌렀습니다.'

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

    return '알림 전송 완료', 200
