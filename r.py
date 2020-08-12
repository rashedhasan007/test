from PIL import Image    
import pytesseract 
#pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
print (pytesseract.image_to_string(Image.open('bangla.png'), lang='ben'))
