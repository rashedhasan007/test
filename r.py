from PIL import Image    
import pytesseract as tess

print tess.image_to_string(Image.open('bangla.jpg'), lang='ben')
