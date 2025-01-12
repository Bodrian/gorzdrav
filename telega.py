#данная программа отвечает за отправку уведомлений из телеграмм пользователю
from notifiers import get_notifier
from key import token_bot, person_id_boris, person_id_olya #файл с ключами

token = token_bot #сюда пишем "token to access the HTTP API" от @BotFather телеграмм

#функция отправляет сообщение
def sent_message(message, name='Boris'):
    if name == 'Olya':
        print(name)
        chat_id = person_id_olya #сюда пишем "Current chat ID:" его узнаем @ifiers телеграм
    else:
        chat_id = person_id_boris
    telegram = get_notifier('telegram')
    message_text = message
    telegram.notify(token=token, chat_id = chat_id, message=message_text)