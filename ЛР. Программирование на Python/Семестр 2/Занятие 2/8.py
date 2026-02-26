class Money:
    def __init__(self, s, money):
        self.s = s
        self.money = money

    def __add__(self, other):
        if other.money == self.money:
            return Money(self.s + other.s, self.money)
        else:
            raise ValueError('Складывать можно только одинаковые валюты')
        
    def __sub__(self, other):
        if other.money == self.money:
            return Money(self.s - other.s, self.money)
        else:
            raise ValueError('Вычитать можно только одинаковые валюты')
        
    def __str__(self):
        return f'{self.s} {self.money}'
    
    def __eq__(self, other):
        return self.s == other.s
    
    def __bool__(self):
        return self.s != 0
    
    def __float__(self):
        return self.s