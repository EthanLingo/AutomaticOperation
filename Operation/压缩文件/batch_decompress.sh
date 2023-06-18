# 对当前文件夹内所有`zst`格式文件批量解压。压缩完一个文件就删除对应的原文件。

find . -name "*.zst" -exec zstd -d --rm {} \;