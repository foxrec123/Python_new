#3. Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
#При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
#Ответить себе на вопрос удобно ли так делать?

import requests
import re

def get_text():
    response = requests.get('https://habrahabr.ru/')
    return response.text


def find_links(text):
    text = get_text()

    pattern = '"(https:.*/)"'
    links = re.findall(pattern, text)
    for i in links:
        print(i)



if __name__ == '__main__':
    text = get_text()
    find_links(text)