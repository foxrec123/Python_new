from random import randint


#1. gen which returns random number
def random_number():
    number = randint(1, 1000)
    while True:
        yield number
        number = randint(1, 1000)


#2. gen is like range
def new_range(a, b, step):
    i = a
    while i < b:
        yield i
        i += step


#3. gen is like map
def new_map(some_list, func):
    number = func(some_list[0])
    i = 0
    while i < len(some_list):
        yield number
        i += 1
        number = func(some_list[i])


#4.gen is like enumerate
def new_enumerate(some_list):
    index, item = 0, some_list[0]
    i = 0
    while i < len(some_list):
        yield index, item
        i += 1
        index, item = i, some_list[i]

#5. gen is like zip
def new_zip(list_1, list_2):
    item_1, item_2 = list_1[0], list_2[0]
    i = 0
    while i < len(list_1):
        yield item_1, item_2
        i += 1
        item_1, item_2 = list_1[i], list_2[i]


#gen = random_number()
#gen = new_range(0, 25, 5)
#gen = new_map([1, 2, 3, 4, 5, 6], lambda x: x * 3)
#gen = new_enumerate([1, 2, 3, 4, 5, 6])
gen = new_zip(['a', 'b', 'c'], [1, 2, 3])

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))