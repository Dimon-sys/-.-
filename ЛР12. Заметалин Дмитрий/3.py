#Вариант10
if __name__ == "__main__":
    from math import *
    def y(x, a=5, b=6, c=7) -> float:
        """
        a > 0
        """
        try: 
            if log10(a) < x:
                return (b**2 + (abs(x+c))**0.5) ** (1/3)
            elif log10(a) == x:
                return cos(x - b - c)
            else:
                return sin(x + a - b)
        except ValueError:
            return "Ошибка: логарифм не определён для отрицательных чисел и нуля"
        
    x = float(input('x='))
    print(y(x))