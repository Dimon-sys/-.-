class Student:
    def __init__(self, name, age, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)
    
    def has_excellent_grades(self):
        return 5 in self.grades
    
s = Student("Иванов И.И.", 20, [4, 5, 4, 5])
print(s.average_grade()) # 4.5
print(s.has_excellent_grades()) # true    
        