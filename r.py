
from flask import Flask, request #import main Flask class and request object
import io
import requests
from io import BytesIO
import pytesseract
from PIL import Image
app = Flask(__name__) #create the Flask app

@app.route('/')
def main():
    return '''<h1>use query-example?=language=passurl</h>'''
@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    response = requests.get(language)
    pytesseract.pytesseract.tesseract_cmd = r'./Tesseract-OCR/tesseract'
    # print( type(response) ) # <class 'requests.models.Response'>
    #img = Image.open(io.BytesIO(response.content))
    img = Image.open(BytesIO(response.content))
    # Convert to gray
    #img=img.convert('L')
    text = pytesseract.image_to_string(img,lang="ben")

    return '''<h1>The language value is: {}</h1>'''.format(text)

if __name__=="__main__":
    app.run()
