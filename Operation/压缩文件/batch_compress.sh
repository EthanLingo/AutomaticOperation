
# 对当前文件夹内所有文件和子文件夹内的文件批量压缩成zst格式。所有的压缩文件设置压缩级别`-3`。压缩完一个文件就删除对应的原文件。

#!/bin/bash
for file in ./*; do
    if [[ -f "$file" ]]; then
        zstd --rsyncable -3 "$file" -o "$file.zst" --rm
    fi
done


