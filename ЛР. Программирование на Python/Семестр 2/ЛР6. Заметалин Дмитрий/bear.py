from PIL import Image, ImageDraw

img = Image.new("RGB", (600, 600), "#E0E0E0")
draw = ImageDraw.Draw(img)

outline_col = "#505050" # Темно-серый контур
white = "white"


    # Средняя часть
draw.ellipse([60, 200, 280, 600], fill=white, outline=outline_col, width=2)
    # Нижняя часть (туловище)
draw.ellipse([150, 450, 330, 600], fill=white, outline=outline_col, width=2)
    # Нижняя часть (лапа)
draw.ellipse([260, 550, 400, 600], fill=white, outline=outline_col, width=2)
    # Голова
draw.ellipse([150, 100, 320, 220], fill=white, outline=outline_col, width=2)
    # Глаза и детали головы
draw.ellipse([210, 150, 215, 155], fill="black") # Глаза
draw.ellipse([150, 110, 170, 130], fill=white, width=2, outline="black") # Ухо
    # Нос
draw.ellipse([315, 150, 325, 160], fill="black")
    # рот
draw.line([290, 180, 312, 180], fill="black")
    # Лунка
draw.ellipse([350, 450, 550, 520], fill="#1A433F", outline="black")
    # Удочка 
draw.line([260, 400, 530, 50], fill="black", width=3) # Удилище
draw.line([530, 50, 530, 480], fill="black", width=1) # Леска
    # Лапа с удочкой
draw.ellipse([210, 330, 310, 370], fill=white, outline=outline_col, width=2)

    # Рыбки 
def draw_fish(x, y):
    draw.ellipse([x, y, x+40, y+20], fill="#95B3D7", outline=outline_col)
    draw.polygon([x, y+10, x-10, y, x-10, y+20], fill="#C0504D") # Хвост

draw_fish(400, 530)
draw_fish(450, 560)
draw_fish(490, 540)

img.save("polar_bear.png")
