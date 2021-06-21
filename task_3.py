"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт,
автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными.
"""

import yaml

data = {"first": ["Rick", "and", "Morty"], "second": 5,
        "third": {"another": "12€", "one_more_time": "4Ç"}}

with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=True, allow_unicode=True)

with open('file.yaml', encoding='utf-8') as yaml_file_for_read:
    yaml_data = yaml.safe_load(yaml_file_for_read)
    print(yaml_data)