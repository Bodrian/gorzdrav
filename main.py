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
    spec(f'https://gorzdrav.spb.ru/_api/api/v2/schedule/lpu/{num_hosp}/speciality/{num_spec}/doctors')
    num_vrach = input('Введите номер врача:  ')
    while True:
        print(f'{time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())} - работаю')
        num = numer(f'https://gorzdrav.spb.ru/_api/api/v2/schedule/lpu/{num_hosp}/doctor/{num_vrach}/appointments')
        if numer_l != num:
            print(num)
            numer_l = num
            for i in numer_l:
                sent_message(i)
                sent_message(i, 'Olya')
        time.sleep(60)

