import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os

im = Image.open("test.jpg") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
text = pytesseract.image_to_string(Image.open("test.jpg"),lang="ben")
print(text)
