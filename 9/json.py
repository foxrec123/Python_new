#2.Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
#(сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
#выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

import requests

def get_information():
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    print(r.status_code)
    print(r.headers)


if __name__ == '__main__':
    get_information()
