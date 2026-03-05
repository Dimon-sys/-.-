#Вариант10
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'


class ShoppingChart:
    def __init__(self, items):
        self.items = items[:]
        if len([i for i in items if isinstance(i, Item)]) != len(items):
            raise TypeError('Не все объекты являются объектами Item!')

    def append(self, other):
        if not isinstance(other, Item):
            raise TypeError('В корзину можно добавлять только объекты Item!')
        else:
            self.items.append(other)

    def __delitem__(self, key):
        if not(-self.__len__() <= key <= self.__len__()-1):
            raise IndexError('Индекс вне списка корзины!')
        else:
            del self.items[key]

    def __len__(self):
        return len(self.items)

    def sum(self):
        return sum([i.price * i.quantity for i in self.items])

    def __str__(self):
        return f'ShoppingChart: {[i.__str__() for i in self.items]}'

book = Item('книга', 500, 1)
pens = Item('ручка', 100, 4)
chart = ShoppingChart([book])
print(chart)
print(len(chart))
chart.append(pens)
print(chart)
print(len(chart))
del chart[0]
print(chart)
print(chart.sum())
