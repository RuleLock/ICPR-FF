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
