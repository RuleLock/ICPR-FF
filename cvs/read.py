import pandas as pd


# 获取tvs实例
def read_tvs(file_name):
    return pd.read_csv(file_name, sep='\t', header=0)


# 获取tvs的行数
def get_tvs_row_num(tvs):
    return tvs.__len__()


# 读取tvs指定行指定key的值
def read_value(tsv, row, key):
    return str(tsv.ix[row, key])


def get_text_rect(char_dict):
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
            right = right_list[index]
            bottom = bottom_list[index]
            char_str = str('%d,%d,%d,%d,%d,%d,%d,%d,%s' % (left, top, left, bottom, right, bottom, right, top, char))
            list.append(char_str)
    return list

