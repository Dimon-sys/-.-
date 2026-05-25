#Вариант10
from PIL import Image, ImageDraw
import os

name = 'eight.jpg'
fullname = os.path.join(f'{os.getcwd()}//eight.jpg')
image = Image.open(fullname).convert('RGBA')

#Маска
mask = Image.new('L', image.size, 0)
draw_mask = ImageDraw.Draw(mask)
width, height = image.size
draw_mask.ellipse([0, 0, width, height], fill=255)

#Копируем изображение и применяем к нему маску
result = image.copy()
result.putalpha(mask)
result.save('eight_oval.png')

#Рисуем черный фон того же размера, что и оригинальное изображение
bg = Image.new('RGBA', (width, height), 'black')
final_image = Image.alpha_composite(bg, result)
final_image.save('eight_border.png')