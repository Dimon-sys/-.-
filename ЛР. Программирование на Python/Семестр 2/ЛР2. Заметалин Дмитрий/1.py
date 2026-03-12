#Вариант10
class Complex:
    def __init__(self, re, im):
        if not((isinstance(re, int) or isinstance(re, float)) and (isinstance(im, int) or isinstance(im, float))):
            raise ValueError('Недопустимый тип аргументов!')
        else:
            self.re = re
            self.im = im

    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5
    
    def arg(self):
        from math import atan
        return atan(self.im/self.re)
    
    def __str__(self):
        if self.im == 0:
            return f'{self.re}'
        elif self.re == 0:
            return f'{self.im}'
        else:
            return f'{self.re}+{self.im}i'
    
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re+other.re, self.im+other.im)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other, self.im)
        else:
            raise ValueError('Недопустимый тип слагаемых!')

    def __radd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Complex):
            p = Complex(-other.re, -other.im)
        elif isinstance(other, int) or isinstance(other, float):
            p = -other
        self.__add__(p)

    def conjugacy(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.re == other
        elif isinstance(other, Complex):
            return (self.re == other.re and self.im == -other.im)
        else:
            raise ValueError('Входные данные могут быть только числами!')
        
z = Complex(3, 4)
print(z)
print(abs(z))
print(z.arg())
a = z + 5
print(a)
b = Complex(3, -4)
print(b.conjugacy(z))
print(a+b)