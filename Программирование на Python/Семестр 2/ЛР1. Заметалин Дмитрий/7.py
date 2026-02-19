class Task:
    def __init__(self, title, description, status='новая'):
        self.title = title
        self.description = description
        self.status = status

    def mark_in_progress(self):
        self.status = 'в процессе'

    def mark_done(self):
        self.status = 'выполнена'

    def update_description(self, new_desc):
        self.description = new_desc

    def is_done(self):
        return self.status == 'выполнена'
    
    def __str__(self):
        return f'Название задачи: {self.title}\nОписание: {self.description}\nСтатус: {self.status}'
    




