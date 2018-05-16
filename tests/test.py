import pytesseract
from PIL import Image
import os

path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path, '2.jpg')
image = Image.open(path)

list = []
list.append('aa')
print(list.__len__())

