class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
    def is_freezing(self):
        return self.celsius < 0
    
t = Temperature(-5)
print(t.to_fahrenheit()) # 23
print(t.is_freezing()) # true