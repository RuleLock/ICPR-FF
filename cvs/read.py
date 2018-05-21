import pandas as pd


# 获取tvs实例
from PIL import Image


def read_tvs(file_name):
    return pd.read_csv(file_name, sep='\t', header=0)


# 获取tvs的行数
def get_tvs_row_num(tvs):
    return tvs.__len__()


# 读取tvs指定行指定key的值
def read_value(tsv, row, key):
    return str(tsv.ix[row, key])


def get_text_rect(char_dict, path):
    image = Image.open(path)
    image_width = image.width
    image_height = image.height
    list = []
    char_list = char_dict.get('char')
    left_list = char_dict.get('left')
    top_list = char_dict.get('top')
    right_list = char_dict.get('right')
    bottom_list = char_dict.get('bottom')
    for char in char_list:
        if char != '~':
            index = char_list.index(char)
            left = left_list[index]
            top = top_list[index]
            top = image_height - top
            right = right_list[index]
            bottom = bottom_list[index]
            bottom = image_height - bottom
            char_str = str('%d,%d,%d,%d,%d,%d,%d,%d,%s' % (left, top, left, bottom, right, bottom, right, top, char))
            # print('left %d top %d right %d bottom %d char %s' % (left, top, right, bottom, char))
            # print('result %s ' % char_str)
            list.append(char_str)
    return list

