from tkinter import *

root = Tk()
root.title('Учебные курсы')
root.geometry('1000x700')
root.resizable(0,0)

math_ico = PhotoImage(file='icos/math.png')
rus_ico = PhotoImage(file='icos/rus.png')
physx_ico = PhotoImage(file='icos/physx.png')
it_ico = PhotoImage(file='icos/it.png')
soc_ico = PhotoImage(file='icos/soc.png')
en_ico = PhotoImage(file='icos/en.png')
history_ico = PhotoImage(file='icos/story.png')
geography_ico = PhotoImage(file='icos/geo.png')
literature_ico = PhotoImage(file='icos/lit.png')


main_menu = Menu(root)

#Меню "Мои курсы"
course_menu = Menu(main_menu, tearoff=0)
course_menu.add_command(label="Мои курсы", compound="left")
course_menu.add_command(label="Добавить курс", compound="left")

#Меню "Каталог" - инициация
catalog_menu = Menu(main_menu, tearoff=0)

#Подменю "Разделы" меню "Каталог"
genres_menu = Menu(catalog_menu, tearoff=0)
genres_menu.add_command(label='Математика', image=math_ico, compound=LEFT)
genres_menu.add_command(label='Русский язык', image=rus_ico, compound="left")
genres_menu.add_command(label='Физика', image=physx_ico, compound="left")
genres_menu.add_command(label='Информатика', image=it_ico, compound="left")
genres_menu.add_command(label='Обществознание', image=soc_ico, compound="left")
genres_menu.add_command(label='Иностранный язык', image=en_ico, compound="left")
genres_menu.add_command(label='История', image=history_ico, compound="left")
genres_menu.add_command(label='География', image=geography_ico, compound="left")
genres_menu.add_command(label='Литература', image=literature_ico, compound="left")

#Подменю "Фильтры" меню "Каталог"
filters_menu = Menu(catalog_menu, tearoff=0)
filters_menu.add_command(label='По длительности')
filters_menu.add_command(label='По дате добавления')
filters_menu.add_command(label='По рейтингу')
filters_menu.add_command(label='По сложности')
filters_menu.add_command(label='По дате ближайшего занятия')

#Меню "Каталог"
catalog_menu.add_command(label='Популярное', compound=LEFT)
catalog_menu.add_command(label='Все', compound="left")
catalog_menu.add_cascade(label='Разделы', menu=genres_menu)
catalog_menu.add_cascade(label='Фильтры', menu=filters_menu)
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

#Контекстное меню
ctxt_menu = Menu(root, tearoff=0)
ctxt_menu.add_command(label='Копировать')
ctxt_menu.add_command(label='Вырезать')
ctxt_menu.add_command(label='Вставить')
ctxt_menu.add_command(label='Удалить')
ctxt_menu.add_command(label='Пометить')

def show_context_menu(event):
    ctxt_menu.post(event.x_root, event.y_root)

root.bind("<Button-3>", show_context_menu)


#Главное меню
main_menu.add_cascade(label='Курсы', menu=course_menu)
main_menu.add_cascade(label='Каталог', menu=catalog_menu)
main_menu.add_cascade(label='Расписание', menu=schedule_menu)
main_menu.add_cascade(label='Домашнее задание', menu=hometask_menu)
main_menu.add_cascade(label='Связь', menu=help_menu)

root.config(menu=main_menu)

root.mainloop()