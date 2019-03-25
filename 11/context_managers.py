from contextlib import contextmanager
from datetime import datetime

#1. Сделать менеджер контекста, который может переопределить
#    значение lock на True внутри блока контекста.

#a) by class
class Lock(object):
    def __init__(self):
        self.lock = False

    def __enter__(self):
        self.lock = True
        return self

    def __exit__(self, *args):
        print('Done!')

#b) by decorator
@contextmanager
def locker(value):
    value = True
    yield value
    print('Done')

#2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные
#   в теле и писал их в консоль, пример использования:


#b) by decorator
@contextmanager
def no_exceptions():
    try:
        yield
    except Exception as e:
        print('{} happend!'.format(e))


#3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода,
#пример использования:

#a) by class
class TimeIt():
    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, *args):
        self.time = datetime.now() - self.start_time

#b) by decorator
@contextmanager
def time_it_cont():
    t = {'time': 0}
    start_time = datetime.now()
    yield t
    end_time = datetime.now()
    t['time'] = end_time - start_time

def long_func():
    p = 0
    for i in range(1, 100000000):
        p = p + i
    print(p)

if __name__ == '__main__':
    #with Lock() as l:
    #    print(l.lock)

    #value = False
    #with locker(value) as l:
    #    print(l)
    # with no_exceptions():
    #     1/0

    # with TimeIt() as t:
    #     long_func()
    #
    # print('Execution time was:', t.time)

    with time_it_cont() as t:
        long_func()
    print('Execution time was:', t['time'] )
