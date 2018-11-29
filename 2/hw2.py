# sorting of numbers
from typing import Tuple


def sort_list():
    my_list = [6, 8, 1, 3, 5, 9]

    my_list.sort()
    print(my_list)

# task with dicts
def task_with_dict():
    my_dict = {1:'Sergei', 2:'Victor', 3:'Natasha', 4:'Stepan', 5:'Igor', 6:'Alex'}

    for key, value in my_dict.items():
        print(key, '  ', value)

# search of minimal value in tuple
def find_max_mix_in_tuple():
    my_tuple = (1.2, 4.5, 6.7, 2.4, 9.7, 5.4)

    print(max(my_tuple))
    print(min(my_tuple))

# to connect words
def connect_words():
    L = ['Earth', 'Russia', 'Moscow']

    string = '->'.join(L)

    print(string)


# to divide string
def divide_string():
    s = '/bin:/usr/bin:/usr/local/bin'

    print(s.split(':'))


# able to divide on 100
def able_to_divide():
    for i in range(1, 101):
        if i % 7 == 0:
            print('{} is divided on 7'.format(i))
        else:
            print('{} is not divided on 7'.format(i))

# matrix_3_4
def matrix_3_4():
    matrix = [
        [12, 15, 20, 96],
        [52, 45, 52, 37],
        [14, 25, 86, 56],
    ]

    print('Strings: ')

    for string in matrix:
        print(string)

    print('Rows: ')

    list_1 = list()
    list_2 = list()
    list_3 = list()
    list_4 = list()

    for row in matrix:
        list_1.append(row[0])
        list_2.append(row[1])
        list_3.append(row[2])
        list_4.append(row[3])

    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)


# print index and element

def print_index_and_element():
    L = ['Hello', 2, 5]

    for i, item in enumerate(L):
        print('{}:{}'.format(i, item))

#to delete
def to_delete():
    L = ['to-delete', 1, 5, 'to-delete', True, 'to-delete']

    while True:
        try:
            L.remove('to-delete')
        except:
            print(L)
            break





if __name__ == '__main__':

    #sort_list()
    #task_with_dict()
    #find_max_mix_in_tuple()
    #connect_words()
    #divide_string()
    #able_to_divide()
    #matrix_3_4()
    #print_index_and_element()
    to_delete()