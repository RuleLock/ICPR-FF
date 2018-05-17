import codecs
def write(file_path, text):
    # text = text.decode('utf-8')
    file = codecs.open(file_path, mode='a', encoding='utf-8')
    file.write(text)
    file.write('\n')
