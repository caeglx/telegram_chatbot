import requests

def send_message(token: str, chat_id: int, message: str):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
    print(requests.get(url).json())