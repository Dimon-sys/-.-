from PIL import Image, ImageDraw, ImageFilter

bear_image = Image.open('polar_bear.png')

im_width, im_height = bear_image.size

bear_resized = bear_image.resize((200, 200))
bear_resized.save('bear_resized_1.png')