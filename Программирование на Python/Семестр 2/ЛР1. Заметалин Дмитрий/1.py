import math

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
    
    def angles(self):
        alfa  = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2)/(2*self.b*self.c)))
        beta  = math.degrees(math.acos((self.b**2 + self.a**2 - self.c**2)/(2*self.b*self.a)))
        gamma = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2)/(2*self.a*self.c)))
        return(alfa, beta, gamma)
    
    def is_isoscele(self):
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        return False
    
    def is_right(self):
        a = round(self.a, 9)
        b = round(self.b, 9)
        c = round(self.c, 9)
        if (a**2 == b**2 + c**2) or (b**2 == c**2 + a**2) or (c**2 == a**2 + b**2):
            return True
        return False
    
    def is_acute(self):
        if (self.a**2 < self.b**2 + self.c**2) or (self.b**2 < self.a**2 + self.c**2) or (self.c**2 < self.a**2 + self.b**2):
            return True
        return False
    
    def is_obtuse(self):
        if (self.a**2 > self.b**2 + self.c**2) or (self.b**2 > self.a**2 + self.c**2) or (self.c**2 > self.a**2 + self.b**2):
            return True
        return False
    
    def triangle_type(self):
        d = ['Треугольник ']
        if self.is_equilateral():
            d += ['равносторонний.']
        elif self.is_isoscele():
            d += [f'равнобедренный, значения углов: {self.angles[0]}, {self.angles[1]}, {self.angles[2]}.']
        else:
            d += [f'имеет разные стороны, значения углов: {self.angles[0]}, {self.angles[1]}, {self.angles[2]}.']