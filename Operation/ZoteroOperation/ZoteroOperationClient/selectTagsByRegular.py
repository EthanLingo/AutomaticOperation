"""
读取 txt 文本的每一行，形成一个列表。根据指定的正则表达式，选择符合条件的元素形成新的列表。
"""

import re

# 读取 txt 文本的每一行，形成一个列表
def readTxtToList(txtPath):
    with open(txtPath, 'r') as f:
        lines = f.readlines() 
    return lines

# # 根据指定的正则表达式，选择符合条件的元素形成新的列表
# def selectTagsByRegular(lines, regular):
#     tags = []
#     for line in lines:
#         tag = re.findall(regular, line)
#         if tag:
#             tags.append(tag[0])
#     return tags

# 读取 txt 文本的每一行，形成一个列表。根据指定的正则表达式，选择符合条件的一些元素形成新的列表
def selectTagsByRegular(txtPath, regular):
    with open(txtPath, 'r') as f:
        lines = f.readlines()
    tags = []
    for line in lines:
        tag = re.findall(regular, line)
        if tag:
            tags.append(tag[0])
    return tags

# 读取 txt 文本的每一行，形成一个列表。根据指定的正则表达式，选择符合条件的行的文本内容形成新的列表
def selectLinesByRegular(txtPath, regular):
    with open(txtPath, 'r') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        tag = re.findall(regular, line)
        if tag:
            new_lines.append(line)
    return new_lines

# 测试
if __name__ == '__main__':
    txtPath = '/Users/ethan/Desktop/所有标签.txt'
    # 正则表达式是，例如对于「【感觉】：重要」，匹配出中括号及其后面的那个冒号。但是不要换行符
    regular = rf'【(.*?)】：(.*?)\n'
    # tags = selectTagsByRegular(txtPath, regular)
    new_lines = selectLinesByRegular(txtPath, regular)
    print(new_lines)
    # 保存 new_lines 到新的 txt 文件
    with open('/Users/ethan/Desktop/所有符合条件的标签.txt', 'w') as f:
        for line in new_lines:
            f.write(line)