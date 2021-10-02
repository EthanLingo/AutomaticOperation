
# TODO 解决Markdown重命名附带重命名附件路径问题


cd "data/mdfiles/"

filepath="original.md"

# 获取旧的文件名name_old、新的文件名name_new；
oldname="original.md"
newname="new original.md"

# 获取存放在Markdown所在项目的文件夹之附件文件夹路径和名称
old_attachment_pathname="${oldname%%.*}.assets"
new_attachment_pathname="${newname%%.*}.assets"

# 对该md文件内部，修改其相对链接之文件夹名为新的文件名：

for oldname in *
do
    if [[ ${filename} =~ ${oldname} ]]
    then
        sed 's/old_attachment_pathname/new_attachment_pathname/' list_tags_original.txt
    fi
done





