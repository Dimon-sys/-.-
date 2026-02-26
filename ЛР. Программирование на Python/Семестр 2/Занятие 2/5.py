class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        
    def __radd__(self, other):
        return self.__add__(other)
    
    def __iadd__(self, other):
        res = self.__add__(other)
        self.x, self.y = res.x, res.y
        return self
    
    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)
    
    def __imul__(self, other):
        res = self.__mul__(other)
        self.x, self.y = res.x, res.y
        return self
    
    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
# Проверка __iadd__ (изменяется существующий)
v4 = Vector(1, 1)
v5 = Vector(2, 2)
old_id_v4 = id(v4)
v4 += v5 #Вызывается __iadd__
print(f"v4 += v5 -> {v4}") # Vector(3, 3)
print(f"id(v4) изменился?: {id(v4)!=old_id_v4}") # False(ID тот же!)
print(f"v4 тот же объект: {id(v4) == old_id_v4}") # true

# Проверка __imul__
v6 = Vector(2, 3)
v6 *= 10
print(f"v6 *= 10 -> {v6}") # Vector(20, 30)