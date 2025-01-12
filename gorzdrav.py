import requests

def get_resp(url): #получает ответ от страницы
    headers = {'User-Agent': 'Chrome/39.0.2171.95 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.ok == True:
            resp = response.json()
            return resp
        else:
            print(f'Проблемы с подключением {print(response)}')
            return False
    except requests.exceptions.Timeout:
        print("Timeout occurred")
    except requests.exceptions.ConnectionError:
        print("No response")
    return False

def hospital(url):
    rez = get_resp(url)
    for i in rez['result']:
        print(f'{i['id']} - {i['address']} - {i['lpuShortName']}')

def spec(url):
    rez = get_resp(url)
    for i in rez['result']:
        print(f'{i['id']} - {i['name']}')

def numer(url):
    numer_list = []
    rez = get_resp(url)
    if rez['message'] != 'Отсутствуют свободные талоны. Попробуйте записаться позже или обратитесь в регистратуру медорганизации':
        for i in rez['result']:
            numer_list.append(i['visitStart'])
    else:
        numer_list = ['нет номерков']
    return numer_list










