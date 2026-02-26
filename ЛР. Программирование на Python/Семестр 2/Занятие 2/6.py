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
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __isub__(self, other):
        res = self.__add__(other.__neg__())
        self.x, self.y = res.x, res.y
        return self
    
v6 = Vector(6, 5)
v5 = Vector(2, 3)
v6 -= v5
print(v6)