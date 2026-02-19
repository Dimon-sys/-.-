class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def is_passed(self):
        if self.grade >= 3:
            return 'Сдал'
        else:
            return 'Не сдал'
        
    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Оценка: {self.grade}'