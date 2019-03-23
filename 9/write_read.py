#1. Реализовать две функции: write_to_file(data) и read_file_data().
#Которые соотвественно: пишут данные в файл и читают данные из файла.

def write_to_file(filename, content):
    with open(filename, mode='w') as f:
        f.write(content)

def read_from_file(filename):
    with open(filename, mode='r') as f:
        print(f.read())


if __name__ == '__main__':
    write_to_file('D:/1.txt', 'Hello, Victor!')
    read_from_file('D:/1.txt')



