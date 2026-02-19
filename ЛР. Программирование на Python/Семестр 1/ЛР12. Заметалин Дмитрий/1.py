#Вариант10
if __name__ == "__main__":
    from math import *
    def f(x):
        return 1.1 * exp(x) + abs(cos((pi*x)**0.5)) - 4/9
    
    n = float(input())
    print(f(n))
