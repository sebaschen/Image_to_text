import pytesseract as tess
from PIL import Image
'''
This file is used to extract the txt from Image
'''
img = Image.open('test.png')
text = tess.image_to_string(img)
print(text)