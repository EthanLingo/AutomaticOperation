from pathlib import Path
import subprocess


def convert_to_docx(root_path, input_tex_file, output_docx_file):
    """
    使用 pandoc 将 LaTeX 文件转换为 DOCX 格式,并生成目录。

    参数:
    root_path (str): 根目录路径
    input_tex_file (str): LaTeX 输入文件的相对路径
    output_docx_file (str): DOCX 输出文件的相对路径
    """
    try:
        # 构建 pandoc 命令
        command = [
            "pandoc",
            f"--resource-path={Path(root_path) / Path(input_tex_file).parent}",
            str(Path(root_path) / Path(input_tex_file)),
            "-o",
            str(Path(root_path) / Path(output_docx_file)),
            "--toc"
        ]

        # 执行 pandoc 命令
        subprocess.run(command, check=True)
        print(f"成功将 {input_tex_file} 转换为 {output_docx_file}")
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")


if __name__ == '__main__':
    # 示例用法
    root_path = "你的路径/GraduationThesis/毕业论文之方案二"
    input_tex_file = "毕业论文之方案二_merged.tex"
    output_docx_file = "毕业论文之方案二_0.docx"

convert_to_docx(root_path, input_tex_file, output_docx_file)
