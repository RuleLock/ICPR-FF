# -*- coding:utf-8 -*-
import os

from cvs import read
from ocr import ocr
from result_io import write_file as write

image_dir_path = os.path.abspath(os.path.dirname(__file__))
image_dir_path = os.path.join(image_dir_path, 'images')
image_file_list = os.listdir(image_dir_path)

current_count = 1

for image in image_file_list:
    image_path = os.path.join(image_dir_path, image)
    char_dict = ocr.get_dict(image_path)
    if char_dict is None:
        print('No.%d. %s error.' % (current_count, image))
        current_count += 1
        continue
    result_list = read.get_text_rect(char_dict)
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, 'outputs')
    file_path = os.path.join(file_path, '%s.txt' % image)
    for result in result_list:
        write.write(file_path, result)
    print('No.%d. %s finish.' % (current_count, image))
    current_count += 1
