class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.grade < other.grade
    
s1 = Student("Alice", 85)
s2 = Student("Alice", 90)
s3 = Student("Bob", 88)
print(s1 == s2) # true
print(s1 < s3) # true