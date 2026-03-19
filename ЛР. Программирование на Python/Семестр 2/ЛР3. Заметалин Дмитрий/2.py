class Employee:

    employees = []

    def __init__(self, thurname, post, income):
        if isinstance(thurname, str) and thurname[0] in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ':
            self.thurname = thurname
        else:
            raise ValueError('Фамилия должна быть строкой и начинаться с заглавной буквы русского алфавита!')
        
        if isinstance(post, str):
            self.post = post
        else:
            raise ValueError('Должность должна быть строкой!')
        
        if isinstance(income, int) or isinstance(income, float) and income >= 0:
            self.income = income
        else:
            raise ValueError('Оклад должен быть неотрицательным числом!')

        Employee.employees.append(self)

    def __repr__(self):
        return f'Employee{self.thurname, self.post, self.income}'
    
    def __str__(self):
        return f'Фамилия: {self.thurname}\nДолжность: {self.post}\nОклад: {self.income}'

    def __del__(self):
        Employee.employees.remove(self)
        print(f'Объект {self.__repr__()} удалён')

    @staticmethod
    def increase_income():
        for employee in Employee.employees:
            employee.income *= 1.15

    @staticmethod
    def ivan_engineer():
        for employee in Employee.employees:
            if employee.thurname.startswith('Иван'):
                employee.post = 'Инженер'


class FacilityEmployee(Employee):

    facilityemployees = []

    def __init__(self, thurname, post, income, rate):
        super().__init__(thurname, post, income)
        if isinstance(rate, int) and 0 <= rate <= 100:
            self.rate = rate
        else:
            raise ValueError('Рейтинг должен быть целым неотрицательным числом от 0 до 100!')
        FacilityEmployee.facilityemployees.append(self)


    @staticmethod
    def increase_income():
        for employee in FacilityEmployee.facilityemployees:
            if 60 <= employee.rate <= 75:
                employee.income *= 1.2
            elif 75 < employee.rate <= 90:
                employee.income *= 1.4
            elif 90 < employee.rate <= 100:
                employee.income *= 1.6

fedorov = FacilityEmployee('Фёдоров', 'Перевозчик', 1000, 60)
FacilityEmployee.increase_income()
print(fedorov.income)
            