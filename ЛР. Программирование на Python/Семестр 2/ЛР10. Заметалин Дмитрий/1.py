from tkinter import *

root = Tk()
root.title('Игрушки')
root.geometry('1000x700')
root.resizable(0,0)

folder_ico = PhotoImage(file='folder.png')
save_ico = PhotoImage(file='save.png')
file_ico = PhotoImage(file='file.png')
brush_ico = PhotoImage(file='brush.png')

main_menu = Menu(root)

#Меню "Файл"
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Новый", compound="left", image=file_ico)
file_menu.add_command(label="Открыть", compound="left", image=folder_ico)
file_menu.add_command(label="Сохранить", compound="left", image=save_ico)
file_menu.add_command(label="Сохранить как", compound="left", image=save_ico)


#Меню "Редактор"
redactor_menu = Menu(main_menu, tearoff=0)

#Подменю "Компоненты"
components_menu = Menu(redactor_menu, tearoff=0)
components_menu.add_command(label='Пружины')
components_menu.add_command(label='Резинки')
components_menu.add_command(label='Твердые компоненты')
components_menu.add_command(label='Трубки')

redactor_menu.add_command(label="Цвет")
redactor_menu.add_command(label="Форма")
redactor_menu.add_cascade(label="Компоненты", menu=components_menu)
redactor_menu.add_command(label="Лепка")
redactor_menu.add_command(label="Соединения")


#Меню "Эскизы"
sketches_menu = Menu(main_menu, tearoff=0)
sketches_menu.add_command(label='Загрузить эскиз')
sketches_menu.add_command(label='Редактировать эскиз', compound='left', image=brush_ico)
sketches_menu.add_command(label='Библиотека')


#Меню "Вид"
view_menu = Menu(main_menu, tearoff=0)
view_menu.add_checkbutton(label='Наименования компонентов')
view_menu.add_checkbutton(label='Стоимость')
view_menu.add_checkbutton(label='Оси координат')


#Главное меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Редактор', menu=redactor_menu)
main_menu.add_cascade(label='Эскизы', menu=sketches_menu)
main_menu.add_cascade(label='Конструктор')
main_menu.add_cascade(label='Шаблоны')
main_menu.add_cascade(label='Помощь')
main_menu.add_cascade(label='Вид', menu=view_menu)

root.config(menu=main_menu)


root.mainloop()