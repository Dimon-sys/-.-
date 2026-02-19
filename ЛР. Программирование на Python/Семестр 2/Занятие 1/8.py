class Calculator:
    def __init__(self, result=0):
        self.result = result

    def add(self, n):
        self.result += n

    def subtract(self, n):
        self.result -= n

    def multiply(self, n):
        self.result *= n

    def divide(self, n):
        if n == 0:
            raise ZeroDivisionError('На ноль делить нельзя!')
        else:
            self.result /= n

    def clear(self):
        self.result = 0

    def get_result(self):
        return self.result
    
calc = Calculator()
calc.add(10)
calc.multiply(2)
calc.subtract(5)
print(calc.get_result())
calc.divide(0)
print(calc.get_result())