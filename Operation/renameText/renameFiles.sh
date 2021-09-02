#!/bin/bash
# Ethan Lin

## 程序：重命名各文件名以正则表达式规则。

## 方法1：（暂时不能用）
# 定义文件夹路径
# cd #your_path.
re="^(.*)(\.md)$"
for filename in *
do
    if [[ ${filename} =~ ${re} ]]
    then
        mv -i "${filename}" "${BASH_REMATCH[1]}\.mmmd"
    fi
done




## 方法2：
find . -name '*.mmd' -exec sh -c '
for filename; do mv "${filename}" "${filename//.mmd/.md}";
done' sh {} +






