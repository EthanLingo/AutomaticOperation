"""
读取 txt 文本的每一行，根据指定的正则表达式，筛选出符合条件的行，存储为新的 txt 文件。
"""

import re

filepath_origin = '/data/original/origin.txt'
filepath_filtered = '/data/original/filtered.txt'

# 定义正则表达式
pattern = re.compile(r'^(?!#)(.*)\/(.*)')

filtered_lines = []
with open(filepath_origin, 'r', encoding='utf-8') as f:
    for line in f:
        if pattern.match(line):
            filtered_lines.append(line.strip())

# 将筛选结果写入新的文件
with open(filepath_filtered, 'w', encoding='utf-8') as f:
    for line in filtered_lines:
        f.write(line + '\n')

print(f"筛选结果已保存到 {filepath_filtered}")
