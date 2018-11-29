#1. process errors
def process_errors():
    number = int(input('Enter a number \n'))
    # even number
    try:
        if number % 2  == 0:
            raise ValueError
    except ValueError:
        print('Number is even')

    # less than 0
    try:
        if number < 0:
            raise TypeError
    except TypeError:
        print('Number is less than 0')

    # more than 10
    try:
        if number > 10:
            raise IndexError
    except IndexError:
        print('Number is more than 10')

#2. get item on index
def get_item_on_index():
    my_list = [1, 5, 8, 34, 54, 23]

    index = int(input('Enter index of the object \n'))
    try:
        print(my_list[index])
    except:
        print('Index is out of range!')

# max of three arguments
def find_two_max_of_three(one, two, three):
    my_list = [one, two, three]
    my_list.sort()
    print('Max numbers are {} and {}'.format(my_list[1], my_list[2]))

# max and min
def max_and_min(*numbers):
    my_list = list(numbers)
    print('Min {}'.format(min(my_list)))
    print('Max {}'.format(max(my_list)))

# join strings
def join_strings(*strings, glue = ':'):
    new_list = []
    for item in strings:
        if len(item) > 3:
            new_list.append(item)

    result = glue.join(new_list)
    print(result)

if __name__ == '__main__':

    #process_errors()
    #get_item_on_index()
    #find_two_max_of_three(15, 2, 5)
    #max_and_min(7, 5, 67, 8, 90, 125)
    join_strings('Alex', 'Sergei', 'Sasha', 'Ya','Roman', 'Tr',glue = '>')