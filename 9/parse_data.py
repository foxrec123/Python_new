import re

def parse_file():
    with open(r'D:\1.txt') as f:
        information = []
        content = f.read()
        pattern = '\d\d/\D\D\D/\d\d\d\d'
        dates = re.findall(pattern, content)
        print(dates)

        pattern = '(django.db.*):'
        locations = re.findall(pattern, content)
        print(locations)

        pattern = '\D:(\d*)'
        strings = re.findall(pattern, content)
        print(strings)

        pattern = '\D:\d*](.*)'
        text = re.findall(pattern, content)
        print(text)


if __name__ == '__main__':
    parse_file()