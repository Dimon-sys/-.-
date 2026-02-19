class ShoppingCart:
    def __init__(self, items = []):
        self.items = items[:]

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(l[1] for l in self.items)
    
    def item_count(self):
        return len(self.items)
    
    def __str__(self):
        return f'{self.items}'
    
cart = ShoppingCart()
cart.add_item("Хлеб", 50)
cart.add_item("Молоко", 80)
print(cart.total()) # 130
print(cart.item_count()) # 2
