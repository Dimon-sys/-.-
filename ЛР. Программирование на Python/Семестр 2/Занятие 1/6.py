class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
    
    def is_origin(self):
        return self.x == 0 and self.y == 0
    
    def __str__(self):
        return self.x, self.y
    
p1 = Point(3, 4)
p2 = Point(0, 0)
print(p1.distance_to(p2))