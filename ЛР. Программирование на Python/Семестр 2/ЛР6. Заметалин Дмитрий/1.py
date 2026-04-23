from PIL import Image, ImageDraw, ImageFilter

width = 700
height = 1000
im = Image.new('RGB', (width, height), (0, 255, 255))
draw = ImageDraw.Draw(im)

draw.rectangle(((0, height*0.55), (width, height)), fill='#E0E0E0', outline=(0,0,0,0))

#Рисуем солнце
size = (500, 500)
    
glow_layer = Image.new("RGBA", size, (0, 0, 0, 0))
draw_glow = ImageDraw.Draw(glow_layer)
    
center_x, center_y = size[0] // 2, size[1] // 2
radius = 180
thick = 14
color = (247, 252, 151)

draw_glow.ellipse([center_x - radius, center_y - radius, 
                       center_x + radius, center_y + radius], 
                      outline=color, width=thick)
draw_glow.line([center_x - radius, center_y, center_x + radius, center_y], 
                   fill=color, width=thick)
draw_glow.line([center_x, center_y - radius, center_x, center_y + radius], 
                   fill=color, width=thick)


blurred_glow = glow_layer.filter(ImageFilter.GaussianBlur(radius=12))


im.paste(blurred_glow, (200, -100), blurred_glow) # Свечение
im.paste(glow_layer, (200, -100), glow_layer)     # Четкие линии поверх

bear_image = Image.open('bear_resized_1.png')
bear_t_image = Image.open('bear_transposed.png')
bear_b_image = Image.open('bear_resized_2.png')

im.paste(bear_image, (20, 760))
im.paste(bear_t_image, (500, 580))
im.paste(bear_t_image, (200, 555))
im.paste(bear_b_image, (370, 780))


im.save('10.png', 'PNG')


