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

ivanov = Employee('Иванов', 'Главный слесарь', 100)
romanov = Employee('Романов', 'Cлесарь', 200)
Employee.increase_income()
print(ivanov.income, romanov.income)
Employee.ivan_engineer()
print(ivanov.post)
print(ivanov)