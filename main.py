import os

from cvs import read
from ocr import ocr
from result_io import write_file as write

image_dir_path = os.path.abspath(os.path.dirname(__file__))
image_dir_path = os.path.join(image_dir_path, 'images')
image_file_list = os.listdir(image_dir_path)

for image in image_file_list:
    image_path = os.path.join(image_dir_path, image)
    char_dict = ocr.get_dict(image_path)
    result_list = read.get_text_rect(char_dict)
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, 'ss.txt')
    for result in result_list:
        write.write(file_path, result)