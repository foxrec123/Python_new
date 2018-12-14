# *ЗАДАЧА 2:
# Пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник
#
# вычисляем периметр и площадь. выводим в консоль.
# можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами.

from math import sqrt

class Square():
    def __init__(self, side):
        self.side = side
        print('Square has been built')

    def calc_square(self):
        return self.side * self.side

    def calc_perimeter(self):
        return self.side * 4


class Rectangle():
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        print('Rectangle has been built')

    def calc_square(self):
        return self.side1 * self.side2

    def calc_perimeter(self):
        return (self.side1 + self.side2) * 2


class Triangle():
    def __init__(self, side1, side2, side3):
        #checking of possibilty of creation Triangle
        sides = [side1, side2, side3]
        largest_side = max(sides)
        sides.remove(largest_side)
        sum_other_sides = sides[0] + sides[1]

        if largest_side >= sum_other_sides:
            raise ValueError('Sides are not appropriate to create triangle')

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        print('Triangle has been built')

    def calc_square(self):
        p = self.calc_perimeter() / 2
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def calc_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Polygon():
    def __init__(self, side1, side2, side3, side4):
        sides = [side1, side2, side3, side4]
        largest_side = max(sides)
        sides.remove(largest_side)
        sum_other_sides = sides[0] + sides[1] + sides[2]

        if largest_side >= sum_other_sides:
            raise ValueError('Sides are not appropriate to create polygon')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        print('Polygon has been built')

    def calc_square(self):
        return 0

    def calc_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4


if __name__ == '__main__':
    sides = input('Enter sides: ')
    sides = sides.strip().split(' ')
    try:
        if len(sides) == 1:
            shape = Square(int(sides[0]))
        elif len(sides) == 2:
            shape = Rectangle(int(sides[0]), int(sides[1]))
        elif len(sides) == 3:
            shape = Triangle(int(sides[0]), int(sides[1]), int(sides[2]))
        elif len(sides) == 4:
            shape = Polygon(int(sides[0]), int(sides[1]), int(sides[2]), int(sides[3]))
        else:
            print('It is impossible to build a shape according to entered data. Try again!')
            raise IndexError

        print('Perimeter {}'.format(shape.calc_perimeter()))
        print('Square {}'.format(shape.calc_square()))

    except Exception as e:
        print(e)

