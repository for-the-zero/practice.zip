import os
from xpinyin import Pinyin

def analyze_pinyin(text):
    p = Pinyin()
    pinyin_dict = {}
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            pinyin = p.get_pinyin(char, '')  # 获取全拼拼音
            if pinyin in pinyin_dict:
                pinyin_dict[pinyin].append(char)
            else:
                pinyin_dict[pinyin] = [char]
    return pinyin_dict

def export_to_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in sorted(data.items(), key=lambda x: (len(x[0]), x[0])):
            file.write(key + '\n')

def export_to_txt_with_chars(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in sorted(data.items(), key=lambda x: (len(x[0]), x[0])):
            file.write(''.join(value) + '\n')

def main():
    # 输入文件路径
    input_file = './output.txt'

    # 读取文本文件
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # 分析拼音
    pinyin_dict = analyze_pinyin(text)

    # 导出拼音到txt
    export_to_txt(pinyin_dict, '拼音.txt')

    # 导出汉字到txt
    export_to_txt_with_chars(pinyin_dict, '汉字.txt')

    print("分析完成！")

if __name__ == '__main__':
    main()
