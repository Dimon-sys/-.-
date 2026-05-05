from tkinter import *

root = Tk()
root.title('Города')
root.geometry('500x500')
root.resizable(0,0)

#Закрытие программы
def close():
    root.destroy()

#Обновление списка
def update_list(val):
    global c
    c = val
    count = int(val)
    l_cities.delete(0, END)
    for i in range(count):
        l_cities.insert(END, cities[i])

#Обновление городов
def update_label():
    global l_cities, cur_city
    sel = l_cities.curselection()
    if sel:
        cur_city.grid_remove()
        cur_city = labels[sel[0]]
        cur_city.grid()
    

#Метки городов
cities = ['Вышние Черти', 'Хохотуй', 'Большие Пупсы', 'Лохово', 'Горшки', 'Веселая жизнь', 'Марс', 'Бодуны']
Label(text='Город:', fg='blue', font=('Arial', 9, 'underline')).grid(row=0, column=0)
labels = []
for i in range(8):
    l = Label(text=f'{cities[i]}', fg='black')
    labels.append(l)
cur_city = Label(text='', fg='black')
cur_city.grid()

#Список городов
l_cities = Listbox(width=15, list=7)
l_cities.place(x=95, y=23)
for i in cities:
    l_cities.insert(END, i)

#Линейка
sc = Scale(root, orient=HORIZONTAL, length=400, from_=4, to=8, tickinterval=1, resolution=1, command=update_list)
sc.place(x=5, y=190)

#Кнопки
start_b = Button(text='Пуск', command=update_label)
start_b.place(x=5, y=250)
close_b = Button(text='Закрыть', command=close)
close_b.place(x=50, y=250)


root.mainloop()