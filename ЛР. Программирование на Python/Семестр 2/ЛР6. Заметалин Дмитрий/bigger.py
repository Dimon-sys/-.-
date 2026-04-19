from PIL import Image, ImageDraw, ImageFilter

bear_image = Image.open('bear_transposed.png')

im_width, im_height = bear_image.size

bear_resized = bear_image.resize((400, 400))
bear_resized.save('bear_resized_2.png')