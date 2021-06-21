"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий
выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных
отчета — например, main_data — и поместить в него названия столбцов отчета в
виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и
поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

import re
import csv


def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта',
                  'Тип системы']]

    for num in range(1, 4):
        with open(f'info_{num}.txt') as file:
            for line in file:
                if re.search(r'Изготовитель системы', line):
                    needed_str = line.split(':')[1].strip()
                    os_prod_list.append(needed_str)
                if re.search(r'Название ОС', line):
                    needed_str = line.split(':')[1].strip()
                    os_name_list.append(needed_str)
                if re.search(r'Код продукта', line):
                    needed_str = line.split(':')[1].strip()
                    os_code_list.append(needed_str)
                if re.search(r'Тип системы', line):
                    needed_str = line.split(':')[1].strip()
                    os_type_list.append(needed_str)
        values_list = []
        values_list.append(os_prod_list[num - 1])
        values_list.append(os_name_list[num - 1])
        values_list.append(os_code_list[num - 1])
        values_list.append(os_type_list[num - 1])
        main_data.append(values_list)

    return main_data


def write_to_csv(name_file_csv):
    with open(f'{name_file_csv}.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(get_data())


write_to_csv('some_csv_file')

# код ниже просто для проверки
# with open('some_csv_file.csv', encoding='utf-8') as file:
#     csv_file = csv.reader(file)
#     for row in csv_file:
#         print(row)
