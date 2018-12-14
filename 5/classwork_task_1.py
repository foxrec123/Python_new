# *ЗАДАЧА 1:
# 1. Создать класс корзина, у которого можно выставить разную вместительность для разных объектов.
# В объекты класса корзина можно помещать разные объекты;
# 2. Вам нужно создать класс пакет, в который тоже можно помещать предметы. У него тоже есть вместимость;
# 3. Создать любой класс, объекты которого можно было бы мощешать в корзину и пакет;
# 4. Если вместимости недостаточно, сказать, что объект поместить нельзя.

class Basket():

    def __init__(self, capacity, name):
        self.capacity = capacity
        self.content = []
        self.name = name

    def put(self, item):
        if len(self.content) < self.capacity:
            self.content.append(item)
            print('Your item is put into the {}!'.format(self.name))
        else:
            print('Here is not enough space for this item!')

    def show_content(self):
        print('In the {}:'.format(self.name))
        for item in self.content:
            print(item.name)
        print('\n')


class Package(Basket):
    pass

class Items():
    def __init__(self, name):
        self.name = name

def put_item(obj, item):
    obj.put(item)


item1 = Items('Spoon')
item2 = Items('Fork')
item3 = Items('Knife')

basket1 = Basket(2, 'basket1')
package1 = Package(3, 'package1')

put_item(basket1, item1)
put_item(basket1, item2)
put_item(basket1, item3)

put_item(package1, item1)
put_item(package1, item2)
put_item(package1, item3)

basket1.show_content()
package1.show_content()