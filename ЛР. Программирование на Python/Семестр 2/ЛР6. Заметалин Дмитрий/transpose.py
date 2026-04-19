from PIL import Image

bear = Image.open('bear_resized_1.png')

bear_transposed = bear.transpose(Image.FLIP_LEFT_RIGHT)

bear_transposed.save('bear_transposed.png')