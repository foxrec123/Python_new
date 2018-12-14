# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека

class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.__acquaintance_list__ = []

    def __str__(self):
        return self.name

    def know(self, person):
        self.__acquaintance_list__.append(person)
        person.__acquaintance_list__.append(self)

    def is_known(self, person):
        if person in self.__acquaintance_list__:
            print('{} knows {}'.format(self, person))
        else:
            print('{} does not know {}'.format(self, person))


if __name__ == '__main__':
    Alex = Person(27, 'Alex')
    Victor = Person(18, 'Victor')
    Igor = Person(24, 'Igor')

    Alex.know(Victor)
    Alex.is_known(Victor)
    Alex.is_known(Igor)

