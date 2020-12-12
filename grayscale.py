from PIL import Image, ImageEnhance
img = Image.open('img.jpg')
pixels = img.load()

img1 = img.convert('L')

enhancer = ImageEnhance.Brightness(img1)

new_img = enhancer.enhance(0.9)
new_img.show()
