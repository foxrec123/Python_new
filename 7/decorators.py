#1. Написать декоратор, который отменяет выполнение любой декорированной функций
# и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
from datetime import datetime

def cancelling_of_func(function):
    def inner(*args):
        print('{} is cancelled'.format(function.__name__))
    return inner

@cancelling_of_func
def my_add(x, y):
    return x + y

#2. Реализовать декоратор, который измеряет скорость выполнения функций

def speed_of_func(function):
    def inner():
        begin_time = datetime.now()
        function()
        end_time = datetime.now()
        time_of_exec = end_time - begin_time
        print('Time of execution: {}'.format(time_of_exec))
    return inner

#3. Реализовать декоратор, который будет считать, сколько раз выполнялась функция

class Counter(object):

    quantity = {}

    @staticmethod
    def count_func(function):
        def inner(*args):
            function()
            if function.__name__ in Counter.quantity:
                Counter.quantity[function.__name__] += 1
            else:
                Counter.quantity.update({function.__name__:1})
            print('Number of executions is {}'.format(Counter.quantity[function.__name__]))
        return inner

#4. Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор,
# начато выполнение функции, закончено выполнение функции

def logger(fucntion):
    def inner(*args):
        print('decorator has been created\n')
        print('execution of the fucntion has been started\n')
        fucntion()
        print('execution of the fucntion has been finished\n')
    return inner

#5. + Реализовать декоратор, который будет перехватывать все исключения в функции.
# Если они случились, нужно просто писать в консоль сообщение об ошибке

def catch_error(function):
    def inner(*args):
        try:
            function()
        except Exception as error:
            print(error)
    return inner


#func_for_checking
@logger
@Counter.count_func
@speed_of_func
def long_func():
    p = 0
    for i in range(1, 100000000):
        p = p + i
    print(p)

@Counter.count_func
def my_add2(x, y):
    return x + y

@catch_error
def func_with_mistakes():
    l = [1, 2 ,3 ,5]
    l[6]
    1/0



if __name__ == '__main__':
#1.
    #my_add(1, 2)

#2.
    #long_func()
   # long_func()
    #long_func()
    #my_add2(1, 2)
    #my_add2(1, 2)

    func_with_mistakes()