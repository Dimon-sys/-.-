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
    
    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)
    
    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
v = Vector(1,1)
print(v + 5)
print(5 + v)