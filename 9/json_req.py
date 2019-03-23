#2.Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
#(сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
#выводить в консоль все пары заголовки, сохранять полученный json в файл на диск
from typing import Dict, Any

import requests
from json import dump


def get_information():
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    return r.headers

def write_to_json(headers):
    headers_dict = dict(headers)
    for key, item in headers_dict.items():
        print(key, ':', item)
    with open(r'D:\1.txt', mode='w') as f:
        dump(headers_dict, f, sort_keys=True, indent=4)


if __name__ == '__main__':
    headers = get_information()
    write_to_json(headers)