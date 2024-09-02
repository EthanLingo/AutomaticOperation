from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import RGBColor
import re

def replace_and_format_text(input_file, output_file):
    doc = Document(input_file)
    for paragraph in doc.paragraphs:
        # 获取段落的所有文本
        full_text = ''.join(run.text for run in paragraph.runs)
        
        # 查找并高亮"【TODO】"
        matches_todo = list(re.finditer(r'【TODO】「(.*?)」', full_text))
        for match in matches_todo:
            start, end = match.span()
            apply_highlight(paragraph, start, end, WD_COLOR_INDEX.BRIGHT_GREEN)
        
        # 查找并高亮"【NOTE】"
        matches_note = list(re.finditer(r'【NOTE】「(.*?)」', full_text))
        for match in matches_note:
            start, end = match.span()
            apply_highlight(paragraph, start, end, WD_COLOR_INDEX.TURQUOISE)
        
        # 查找并改变颜色"【文献】"
        matches_reference = list(re.finditer(r'【文献】「(.*?)」.*?\(.*?\)', full_text))
        for match in matches_reference:
            start, end = match.span(1)
            apply_color(paragraph, start, end, RGBColor(0, 0, 255))

    # 保存输出文档
    doc.save(output_file)

def apply_highlight(paragraph, start, end, color):
    current_pos = 0
    for run in paragraph.runs:
        run_length = len(run.text)
        if current_pos + run_length > start:
            highlight_start = max(start - current_pos, 0)
            highlight_end = min(end - current_pos, run_length)
            if highlight_start < highlight_end:
                run.font.highlight_color = color
        current_pos += run_length
        if current_pos >= end:
            break

def apply_color(paragraph, start, end, color):
    current_pos = 0
    for run in paragraph.runs:
        run_length = len(run.text)
        if current_pos + run_length > start:
            color_start = max(start - current_pos, 0)
            color_end = min(end - current_pos, run_length)
            if color_start < color_end:
                run.font.color.rgb = color
        current_pos += run_length
        if current_pos >= end:
            break

if __name__ == '__main__':
    # 示例用法
    input_file = '你的路径/GraduationThesis/毕业论文之方案二/毕业论文之方案二_1.docx'
    output_file = '你的路径/GraduationThesis/毕业论文之方案二/毕业论文之方案二_4.docx'

    replace_and_format_text(input_file, output_file)