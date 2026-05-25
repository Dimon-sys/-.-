#Вариант10
from PIL import Image, ImageFilter

img = Image.open('eight.jpg')
dilated = img.filter(ImageFilter.MaxFilter(3)) #дилатация
closed = dilated.filter(ImageFilter.MinFilter(3)) #эрозия
closed.save('eight_closed.jpg')