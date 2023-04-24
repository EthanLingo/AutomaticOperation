
# %%

from PIL import Image
import os

# 指定目标长宽比
target_ratio = 1080/2412

# 指定背景颜色为金色
bg_color = (255, 215, 0)

# 指定文件夹路径
folder_path_base = "Projects/改图片/data"
folder_path_input = os.path.join(folder_path_base,"input")
folder_path_output = os.path.join(folder_path_base, "output")

# 遍历文件夹中的所有图像文件
for filename in os.listdir(folder_path_input):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # 打开图像文件并获取宽度和高度
        filepath = os.path.join(folder_path_input, filename)
        with Image.open(filepath) as img:
            width, height = img.size
            
            # 计算当前图像的长宽比
            current_ratio = width/height
            
            # 如果当前比例小于目标比例，则在左右两侧添加背景
            if current_ratio < target_ratio:
                new_width = int(height * target_ratio)
                new_img = Image.new("RGB", (new_width, height), bg_color)
                offset = (new_width - width) // 2
                new_img.paste(img, (offset, 0))
            
            # 如果当前比例大于目标比例，则在上下两侧添加背景
            elif current_ratio > target_ratio:
                new_height = int(width / target_ratio)
                new_img = Image.new("RGB", (width, new_height), bg_color)
                offset = (new_height - height) // 2
                new_img.paste(img, (0, offset))
            
            # 如果当前比例已经符合目标比例，则不做任何处理
            else:
                new_img = img
            
            # 保存新图像文件
            new_filename = os.path.splitext(filename)[0] + "_resized.jpg"
            new_filepath = os.path.join(folder_path_output, new_filename)
            new_img.save(new_filepath)

