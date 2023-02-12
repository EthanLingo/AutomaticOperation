
# 解决重命名Markdown文件及其附件问题
# 危险！谨慎使用命令sed。


cd "Projects/解决重命名Markdown文件及其附件问题/data"

# 获取旧的文件名name_old、新的文件名name_new；
# filepath="original copy.md"
oldname="new new original copy.md"
newname="new original copy.md"

# 获取存放在Markdown所在项目的文件夹之附件文件夹路径和名称
old_attachment_pathname="${oldname%%.*}.assets"
new_attachment_pathname="${newname%%.*}.assets"


for filename in *
do
    if [[ ${filename} =~ ${oldname} ]]
    then
        # 改附件链接为新的
        sed -i "" 's/'${old_attachment_pathname}'/'${new_attachment_pathname}'/g' "${filename}"
        # 改旧文件名为新文件名
        mv -i "${filename}" "${newname}"
        # 改旧附件目录名为新附件目录名
        mv -i "${old_attachment_pathname}" "${new_attachment_pathname}"
    fi
done





