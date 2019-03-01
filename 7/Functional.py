
from functools import reduce



if __name__ == '__main__':

# 1. При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]

    result = map(lambda x: x % 5, [1, 4, 5, 30, 99])
    print(list(result))

#2. При помощи map превратить все числа из массива [3, 4, 90, -2] в строки

    result = map(lambda x:str(x), [3, 4, 90, -2])
    print(list(result))

#3. При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки

    result = filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str])
    print(list(result))

#4. При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']

    result = map(lambda x: len(x), ['some', 'other', 'value'])
    result = reduce(lambda x, y: x + y, result)
    print(result)