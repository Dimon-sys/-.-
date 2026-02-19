class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 and b <= 0 and c <= 0:
            raise ValueError('<0')
        if a+b<=c or b+c<=a or c+a<=b:
            raise ValueError('no tr')
        sides = sorted([a,b,c])
        self.a, self.b, self.c = sides

    def __str__(self):
        return f'{self.a},{self.b},{self.c}'

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    def is_equilateral(self, eps=0.0001):
        return abs(self.a-self.b)<=eps and abs(self.b-self.c)<=eps
        
t1 = Triangle(3, 4, 5)
print(t1)
print(t1.perimeter())
print(t1.area())
print(t1.is_equilateral())

