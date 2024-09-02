import re
from pathlib import Path


def merge_single_subfile(subfile_path, output_file):
    subfile_path = Path(subfile_path).resolve()
    with subfile_path.open('r', encoding='utf-8') as f:
        content = f.read()

    # 去掉头部的 \documentclass、\begin{document} 和 \graphicspath 及其紧随其后的内容
    head_patterns = r'(\\documentclass.*?\\begin\{document\}|\\graphicspath\{.*?\})'
    content = re.sub(head_patterns, '', content, flags=re.DOTALL)

    # 去掉尾部的 \end{document}
    tail_patterns = r'\\end\{document\}'
    content = re.sub(tail_patterns, '', content)

    # 使用正则表达式找到所有未被注释的 \subfile 命令
    subfile_patterns = r'(?<!% )\\subfile\{(.*?)\}'
    subfile_matches = re.finditer(subfile_patterns, content)

    last_end = 0
    for match in subfile_matches:
        start, end = match.span()
        nested_subfile_path = match.group(1)
        nested_subfile_path = subfile_path.parent / Path(nested_subfile_path + '.tex')

        # 写入当前部分内容
        output_file.write(content[last_end:start])

        # 递归处理子文件
        merge_single_subfile(nested_subfile_path.resolve(), output_file)

        last_end = end

    # 写入剩余部分内容
    output_file.write(content[last_end:])
    output_file.write('\n\n')


def merge_subfiles(main_file_path, output_file_path):
    main_file_path = Path(main_file_path).resolve()
    output_file_path = Path(output_file_path).resolve()

    with output_file_path.open('w', encoding='utf-8') as f:
        merge_single_subfile(main_file_path, f)

    # 读取合并后的文件内容
    with output_file_path.open('r', encoding='utf-8') as f:
        merged_content = f.read()

    # 去掉"//【"中的"//"
    merged_content = re.sub(r'//【', '【', merged_content)

    # 写回合并后的文件
    with output_file_path.open('w', encoding='utf-8') as f:
        f.write(merged_content)


if __name__ == '__main__':
    # 示例用法
    merge_subfiles(
        '你的路径/GraduationThesis/毕业论文之方案二/毕业论文之方案二.tex',
        '你的路径/GraduationThesis/毕业论文之方案二/毕业论文之方案二_merged.tex'
    )
