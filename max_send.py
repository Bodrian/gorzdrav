''' отправка сообщения через макс для личного пользования '''
import requests
from key import max_user_id_olga, max_user_id_boris, max_token_bot
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Токен бота, от лица которого отправляем сообщения
TOKEN = max_token_bot
API_URL = "https://platform-api2.max.ru/messages"

USER_IDS = {
    "Olya": max_user_id_olga,
    "Boris": max_user_id_boris
}
DEFAULT_USER_ID = max_user_id_boris


def sent_message(text: str, person: str = None):
    user_id = USER_IDS.get(person, DEFAULT_USER_ID)

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    params = {"user_id": user_id}
    payload = {"text": text}

    resp = requests.post(API_URL, json=payload, params=params, headers=headers, verify=False)

    if resp.status_code == 200:
        print(f"Отправлено в MAX (user_id={user_id})")
    else:
        print(f"Ошибка MAX: {resp.status_code} — {resp.text}")