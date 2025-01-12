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
    rez = get_resp(url)
    numer_list = ['нет номерков']
    if rez is not False:
        if rez.get('result') is None:
            numer_list = ['нет номерков']
        else:
            numer_list = []
            for i in rez['result']:
                numer_list.append(i['visitStart'])
    return numer_list










