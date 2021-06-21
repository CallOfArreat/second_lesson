"""
### 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате
JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение
данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""

import json
from datetime import date


def write_order_to_json(item='', quantity=0, price=0, buyer='', date=''):
    with open('orders.json') as json_file:
        json_data = json_file.read()
        json_objects = json.loads(json_data)
        values_dict = {"item": item, "quantity": quantity, "price": price,
                       "buyer": buyer, "date": date}
        json_objects["orders"].append(values_dict)

        # print(json_objects)

    with open('orders.json', 'w', encoding='utf-8') as json_file_1:
        json.dump(json_objects, json_file_1, indent=4)


date_now = str(date.today())

write_order_to_json('notebook', 2, 58000, 'Ivan Ivanov', date_now)
write_order_to_json('PC', 1, 158000, 'Fedor Fedorov', date_now)

# чтобы посмотреть, что всё сработало
# with open('orders.json', encoding='utf-8') as json_file_for_print:
#     json_data = json_file_for_print.read()
#     print(json_data)
