from datetime import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def get_age(self):
        return datetime.now().year - self.year