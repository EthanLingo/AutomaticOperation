"""
设计一个在macos运行的python小程序。实现以下功能：

1. 对于源文件夹【folder_source】内，匹配并获取所有名称开头为「XXX」的文件，得到文件名称列表【list_files_name】。匹配并获取所有名称开头为「XXX」，结尾为「YYY」的文件夹，得到文件夹名称列表【list_folders_name】。注意：不匹配子文件与子文件夹；

2. 根据【list_files_name】，复制新的列表【list_new_names_1】。根据【list_folders_name】，复制新的列表【list_new_names_2】；

3. 列表【list_new_names_1】去掉每一项的「XXX」字符串，去掉后缀名。列表【list_new_names_2】去掉每一项的开头为「XXX」，结尾为「YYY」的字符串。例如【folder_source】匹配到文件【XXXA1】，放在了【list_files_name】当中的某一项的值为「XXXA1」，那么【list_new_names_1】对应的那一项为「A1」；

4. 并集列表【list_new_names_1】、【list_new_names_2】，得到新列表【list_new_names】。备注：这一步是合并去重；

5. 根据【list_new_names】的每一项【new_name】，在目标文件夹【folder_target】依次做：

    1. 新建一个文件夹【folder_i】，名称为【new_name】的值；

    2. 在【list_files_name】匹配【new_name】的项，该项对应的文件移动到【folder_i】；
    
    3. 在【list_folders_name】匹配【new_name】的项，该项对应的文件夹移动到【folder_i】；
"""
# import os
# import shutil


# def move_files(folder_source, folder_target, start_string):
#     # Step 1: 获取匹配的文件和文件夹名称列表
#     files = os.listdir(folder_source)
#     list_files_name = [f for f in files if os.path.isfile(
#         os.path.join(folder_source, f)) and f.startswith(start_string)]
#     list_folders_name = [f for f in files if os.path.isdir(
#         os.path.join(folder_source, f)) and f.startswith(start_string)]

#     os.makedirs(folder_target, exist_ok=True)

#     # Step 2: 复制并处理文件名称列表
#     list_new_names_1 = list_files_name.copy()

#     # Step 3: 去掉每一项的「XXX」字符串和后缀名
#     list_new_names_1 = [name.replace(start_string, '').split('.')[
#         0] for name in list_new_names_1]

#     # Step 4: 复制并处理文件夹名称列表
#     list_new_names_2 = list_folders_name.copy()

#     # Step 5: 去掉每一项的「XXX」字符串
#     list_new_names_2 = [name.replace(start_string, '')
#                         for name in list_new_names_2]

#     # Step 6: 合并去重得到新列表
#     list_new_names = list(set(list_new_names_1 + list_new_names_2))

#     for new_name in list_new_names:
#         folder_i = os.path.join(folder_target, new_name)
#         os.makedirs(folder_i, exist_ok=True)  # 创建目标文件夹，如果已存在则跳过

#         # 处理匹配的文件
#         matching_files = [f for f in list_files_name if f.startswith(
#             start_string + new_name)]
#         for file in matching_files:
#             source_path = os.path.join(folder_source, file)
#             target_path = os.path.join(folder_i, file)
#             if os.path.exists(source_path):
#                 shutil.move(source_path, target_path)

#         # 处理匹配的文件夹
#         matching_folders = [
#             f for f in list_folders_name if f.startswith(start_string + new_name)]
#         for folder in matching_folders:
#             source_path = os.path.join(folder_source, folder)
#             target_path = os.path.join(folder_i, folder)
#             if os.path.exists(source_path):
#                 shutil.move(source_path, target_path)

import os
import shutil


def move_files(folder_source, folder_target, start_string, end_string):
    # Step 1: 获取匹配的文件和文件夹名称列表
    files = os.listdir(folder_source)
    list_files_name = [f for f in files if os.path.isfile(
        os.path.join(folder_source, f)) and f.startswith(start_string)]
    list_folders_name = [f for f in files if os.path.isdir(os.path.join(
        folder_source, f)) and f.startswith(start_string) and f.endswith(end_string)]

    os.makedirs(folder_target, exist_ok=True)

    # Step 2: 复制并处理文件名称列表
    list_new_names_1 = list_files_name.copy()

    # Step 3: 去掉每一项的「XXX」字符串和后缀名
    list_new_names_1 = [name.replace(start_string, '').split('.')[
        0] for name in list_new_names_1]

    # Step 4: 复制并处理文件夹名称列表
    list_new_names_2 = list_folders_name.copy()

    # Step 5: 去掉每一项的开头为「XXX」，结尾为「YYY」的字符串
    list_new_names_2 = [name[len(start_string):-len(end_string)] for name in list_new_names_2]

    # Step 6: 合并去重得到新列表
    list_new_names = list(set(list_new_names_1 + list_new_names_2))

    for new_name in list_new_names:
        folder_i = os.path.join(folder_target, new_name)
        os.makedirs(folder_i, exist_ok=True)  # 创建目标文件夹，如果已存在则跳过

        # 处理匹配的文件
        matching_files = [f for f in list_files_name if f.startswith(
            start_string + new_name)]
        for file in matching_files:
            source_path = os.path.join(folder_source, file)
            target_path = os.path.join(folder_i, file)
            if os.path.exists(source_path):
                shutil.move(source_path, target_path)

        # 处理匹配的文件夹
        matching_folders = [
            f for f in list_folders_name if f.startswith(start_string + new_name)]
        for folder in matching_folders:
            source_path = os.path.join(folder_source, folder)
            target_path = os.path.join(folder_i, folder)
            if os.path.exists(source_path):
                shutil.move(source_path, target_path)


if __name__ == '__main__':
    folder_source = '/Users/ethan/Downloads/s copy'  # 替换为源文件夹的路径
    folder_target = '/Users/ethan/Downloads/t'  # 替换为目标文件夹的路径

    move_files(folder_source, folder_target,
               start_string='设计：', end_string='')
