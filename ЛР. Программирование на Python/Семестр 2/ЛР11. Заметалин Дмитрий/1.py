from tkinter import *

#Начало
root = Tk()
root.title('День недели')
root.geometry('1000x700')
height = 700
width = 1000
k = 0.75
root.resizable(0,0)

days = [['', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'],['', 'ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ']]

#Переменная для хранения значения
r_var = IntVar()
r_var.set(0)

#Изменение IntVar с помощью кнопок и запись в Enter
def text_button():
    ent.delete(0, END)
    ent.insert(0, days[cap_var.get()][r_var.get()])


#Селекторные кнопки
r1 = Radiobutton(text='Понедельник', indicatoron=0, variable=r_var, value=1, command=text_button)
r2 = Radiobutton(text='Вторник', indicatoron=0, variable=r_var, value=2, command=text_button)
r3 = Radiobutton(text='Среда', indicatoron=0, variable=r_var, value=3, command=text_button)
r4 = Radiobutton(text='Четверг', indicatoron=0, variable=r_var, value=4, command=text_button)
r5 = Radiobutton(text='Пятница', indicatoron=0, variable=r_var, value=5, command=text_button)
r6 = Radiobutton(text='Суббота', indicatoron=0, variable=r_var, value=6, command=text_button)
r7 = Radiobutton(text='Воскресенье', indicatoron=0, variable=r_var, value=7, command=text_button)
r1.place(x=width*(1/9), y=height*k)
r2.place(x=width*(2/9), y=height*k)
r3.place(x=width*(3/9), y=height*k)
r4.place(x=width*(4/9), y=height*k)
r5.place(x=width*(5/9), y=height*k)
r6.place(x=width*(6/9), y=height*k)
r7.place(x=width*(7/9), y=height*k)


#Закрытие программы
def close():
    root.destroy()

close_b=Button(text='Закрыть', command=close)
close_b.place(x=width*0.5, y=height*0.9)

#Изменение IntVar с помощью ползунка и запись в Enter
def show_value(event):
    r_var.set(sc.get())
    ent.delete(0, END)
    ent.insert(0, days[cap_var.get()][r_var.get()])



#Ползунок
sc = Scale(root, orient=HORIZONTAL, length=750, from_=1, to=7, variable=r_var, tickinterval=1, resolution=1, command=show_value)
sc.place(x=width*(1/9), y=height*0.8)


#Поле ввода
ent = Entry(root)
ent.place(x=width*0.43, y=height*0.48)
day_of_the_week = Label(root, text='День недели')
day_of_the_week.place(x=width*0.45, y=height*0.45)

#Смена регистра
def switch():
    ent.delete(0, END)
    ent.insert(0, days[cap_var.get()][r_var.get()])

#Флаг смены регистра
cap_var = IntVar()
cap_var.set(0)
cap = Checkbutton(text='Заглавные буквы', variable=cap_var, command=switch)
cap.place(x=width*0.3, y=height*0.48)

root.mainloop()