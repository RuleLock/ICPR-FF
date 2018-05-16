import pytesseract
from pytesseract import Output
from PIL import Image


def get_dict(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_boxes(image, lang='chi_sim+eng', output_type=Output.DICT)
