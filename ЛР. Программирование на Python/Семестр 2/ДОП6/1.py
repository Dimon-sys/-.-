#Вариант10
from PIL import Image
import os

name = 'eight.jpg'
fullname = os.path.join(f'{os.getcwd()}//eight.jpg')
image = Image.open(fullname)
pixels = image.load()
x, y = image.size

def change_rb(pixel):
    r, g, b = pixel
    return b, g, r

for i in range(x):
    for j in range(y):
        pixels[i, j] = change_rb(pixels[i, j])

image.save('eight_rb.jpg')

