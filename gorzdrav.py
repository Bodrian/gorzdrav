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

def district(): #получает словарь районов в формате '1': 'Адмиралтейский',
    distr = {}
    url = 'https://gorzdrav.spb.ru/_api/api/v2/shared/districts'
    rez = get_resp(url)
    for i in rez['result']:
        print(f'{i['id']} - {i['name']}')
        distr[i['id']] = i['name']
    return distr

def hospital(url): #пол
    hospital = {}
    url = 'https://gorzdrav.spb.ru/_api/api/v2/shared/districts'
    rez = get_resp(url)
    for i in rez['result']:
        print(f'{i['id']} - {i['name']}')
        distr[i['id']] = i['name']
    return distr

def rez():
    pass