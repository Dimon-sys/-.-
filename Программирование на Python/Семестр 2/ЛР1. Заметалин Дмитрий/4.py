class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def __str__(self):
        return f'Ширина: {self.width}, Высота: {self.height}'
    
    def is_square(self):
        return self.width == self.height