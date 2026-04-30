import tkinter as tk

# Список из 8 городов
CITIES = [
    "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург",
    "Казань", "Нижний Новгород", "Челябинск", "Омск"
]

class CitySelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор города")
        self.root.geometry("500x400")

        # Словарь для связи названия города с меткой
        self.labels = {}
        # Текущая видимая метка
        self.current_label = None

        # Левая часть: фрейм с метками городов
        self.labels_frame = tk.Frame(root)
        self.labels_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Создаём 8 меток и сразу скрываем их
        for i, city in enumerate(CITIES):
            label = tk.Label(self.labels_frame, text=city, font=("Arial", 12), bg="lightyellow", relief=tk.RIDGE, width=20)
            label.grid(row=i, column=0, pady=2, sticky="w")
            label.grid_remove()    # исходно скрыта
            self.labels[city] = label

        # Правая часть: Listbox, Scale и кнопки
        right_frame = tk.Frame(root)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Listbox для выбора города
        self.listbox = tk.Listbox(right_frame, height=8, font=("Arial", 10))
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Scale для выбора количества городов в списке (от 4 до 8)
        self.scale_var = tk.IntVar(value=8)  # по умолчанию 8
        scale = tk.Scale(right_frame, from_=4, to=8, orient=tk.HORIZONTAL,
                         label="Количество доступных городов:", variable=self.scale_var,
                         tickinterval=1, resolution=1)
        scale.pack(fill=tk.X, pady=(0, 10))

        # Кнопка "Пуск"
        start_btn = tk.Button(right_frame, text="Пуск", command=self.on_start, width=15)
        start_btn.pack(pady=5)

        # Кнопка "Закрыть"
        close_btn = tk.Button(right_frame, text="Закрыть", command=self.on_close, width=15)
        close_btn.pack(pady=5)

        # Отслеживаем изменение значения Scale
        self.scale_var.trace_add("write", self.update_listbox)

        # Инициализация списка городов в Listbox
        self.update_listbox()

    def update_listbox(self, *args):
        """Обновляет содержимое Listbox в соответствии с текущим значением Scale."""
        count = self.scale_var.get()
        # Очищаем Listbox
        self.listbox.delete(0, tk.END)
        # Добавляем первые 'count' городов
        for city in CITIES[:count]:
            self.listbox.insert(tk.END, city)

        # Сбрасываем выделение
        self.listbox.selection_clear(0, tk.END)

        # Если какая-то метка была видима, скрываем её, так как город мог стать недоступным
        self.hide_current_label()

    def hide_current_label(self):
        """Скрывает текущую видимую метку (если она есть)."""
        if self.current_label:
            self.current_label.grid_remove()
            self.current_label = None

    def on_start(self):
        """Обработчик кнопки 'Пуск': показывает метку выбранного города."""
        selected = self.listbox.curselection()
        if not selected:
            # Ничего не выбрано
            return

        city_name = self.listbox.get(selected[0])

        # Если эта метка уже видна, ничего не делаем
        if self.current_label and self.current_label.cget("text") == city_name:
            return

        # Скрываем предыдущую метку и показываем новую
        self.hide_current_label()
        label_to_show = self.labels[city_name]
        label_to_show.grid()   # показываем метку
        self.current_label = label_to_show

    def on_close(self):
        """Завершает программу."""
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CitySelectorApp(root)
    root.mainloop()