import pytesseract as tess
from PIL import Image
'''
This file is used to transfer the picture to txt
'''
img = Image.open('test.png')
text = tess.image_to_string(img)
print(text)