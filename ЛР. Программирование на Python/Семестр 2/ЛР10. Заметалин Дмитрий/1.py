from tkinter import *

root = Tk()
root.title('Учебные курсы')
root.geometry('1000x700')
root.resizable(0,0)

main_menu = Menu(root)

#Меню "Мои курсы"
course_menu = Menu(main_menu, tearoff=0)
course_menu.add_command(label="Мои курсы", compound="left")
course_menu.add_command(label="Добавить курс", compound="left")

#Меню "Каталог" - инициация
catalog_menu = Menu(main_menu, tearoff=0)

#Подменю "Разделы" меню "Каталог"
genres_menu = Menu(catalog_menu, tearoff=0)
genres_menu.add_command(label='Математика', compound="left")
genres_menu.add_command(label='Русский язык', compound="left")
genres_menu.add_command(label='Физика', compound="left")
genres_menu.add_command(label='Информатика', compound="left")
genres_menu.add_command(label='Обществознание', compound="left")
genres_menu.add_command(label='Иностранный язык', compound="left")
genres_menu.add_command(label='История', compound="left")
genres_menu.add_command(label='География', compound="left")
genres_menu.add_command(label='Литература', compound="left")


#Меню "Каталог"
catalog_menu.add_command(label='Популярное', compound="left")
catalog_menu.add_command(label='Все', compound="left")
catalog_menu.add_cascade(label='Разделы', menu=genres_menu)
catalog_menu.add_command(label='Фильтры', compound="left")
catalog_menu.add_command(label='Избранное', compound="left")


#Меню "Расписание"
schedule_menu = Menu(main_menu, tearoff=0)
schedule_menu.add_command(label='На сегодня', compound="left")
schedule_menu.add_command(label='На завтра', compound="left")
schedule_menu.add_command(label='На эту неделю', compound='left')
schedule_menu.add_command(label='На следующую неделю', compound="left")
schedule_menu.add_command(label='На этот месяц', compound="left")


#Меню "Домашнее задание"
hometask_menu = Menu(main_menu, tearoff=0)
hometask_menu.add_command(label='На сегодня', compound="left")
hometask_menu.add_command(label='На завтра', compound="left")
hometask_menu.add_command(label='На эту неделю', compound='left')
hometask_menu.add_command(label='На следующую неделю', compound="left")
hometask_menu.add_command(label='По предметам', compound="left")
hometask_menu.add_command(label='По сложности', compound="left")
hometask_menu.add_command(label='По срокам сдачи', compound="left")


#Меню "Связь"
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label='Справка', compound="left")
help_menu.add_command(label='Обратная связь', compound="left")
help_menu.add_command(label='Помощь', compound="left")
help_menu.add_command(label='Контакты', compound="left")
help_menu.add_command(label='Оставить отзыв', compound="left")


#Главное меню
main_menu.add_cascade(label='Курсы', menu=course_menu)
main_menu.add_cascade(label='Каталог', menu=catalog_menu)
main_menu.add_cascade(label='Расписание', menu=schedule_menu)
main_menu.add_cascade(label='Домашнее задание', menu=hometask_menu)
main_menu.add_cascade(label='Связь', menu=help_menu)

root.config(menu=main_menu)

root.mainloop()