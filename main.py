from gorzdrav import hospital, spec, numer
from telega import sent_message
import time

if __name__ == '__main__':
    numer_l = []
    spec('https://gorzdrav.spb.ru/_api/api/v2/shared/districts') #выводим список районов города
    num_dist = input('Введите номер района:  ')
    hospital(f'https://gorzdrav.spb.ru/_api/api/v2/shared/district/{num_dist}/lpus')
    num_hosp = input('Введите номер мед.учреждения:  ')
    spec(f'https://gorzdrav.spb.ru/_api/api/v2/schedule/lpu/{num_hosp}/specialties')
    num_spec = input('Введите номер специальности:  ')
    doctor_names = spec(f'https://gorzdrav.spb.ru/_api/api/v2/schedule/lpu/{num_hosp}/speciality/{num_spec}/doctors')
    num_vrach = input('Введите номер врача:  ')
    doctor_name = doctor_names[num_vrach].split(' ')[0]
    data_flag = input('Нужна определенная дата? Enter - нет, 1 - да:  ')
    person_flag = input('Ты Оля? Enter - нет, 1 - да:  ')
    if data_flag:
        data = input('Введите числа которые интересны через пробел: ')
        data_list = data.split(' ')
    while True:
        print(f'{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())} - работаю')
        num = numer(f'https://gorzdrav.spb.ru/_api/api/v2/schedule/lpu/{num_hosp}/doctor/{num_vrach}/appointments')

        if data_flag:   #проверка на нужную дату
            num_temp = []
            for i in num:
                for day in data_list:
                    if day == i[8:10]:
                        num_temp.append(i)
            num = num_temp
            if not num:
                num = ['нет номерков']

        if numer_l != num:
            print(num, ' - ' , doctor_name)
            numer_l = num
            for i in numer_l:
                if person_flag:
                    sent_message(f'{i} - {doctor_name}', 'Olya')
                else:
                    sent_message(f'{i} - {doctor_name}')

        time.sleep(45)

