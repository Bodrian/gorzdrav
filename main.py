from gorzdrav import district, hospital

if __name__ == '__main__':
    district() #выводим список районов города
    num_dist = input('Введите номер района:  ')
    hospital(f'https://gorzdrav.spb.ru/_api/api/v2/shared/district/{num_dist}/lpus')
    num_hosp = input('Введите номер мед.учреждения:  ')



