import os

# # 指定文件夹路径
# folder_path = "dual"

# # 获取文件夹下所有文件名
# file_names = os.listdir(folder_path)

# # 创建一个新的文件"filenames.txt"，将文件名逐行保存
# with open("filenames.txt", "w") as file:
#     for file_name in file_names:
#         file.write(file_name + "\n")

# file_path = 'filenames.txt'  # 替换成你的 txt 文件路径

# # 读取原始文件内容
# with open(file_path, 'r') as file:
#     lines = file.readlines()

# # 在每一行前面添加 "video/"
# new_lines = ['video/' + line.strip() for line in lines]

# # 将修改后的内容写回原文件
# with open(file_path, 'w') as file:
#     file.write('\n'.join(new_lines))

# print("每行已添加 'video/' 前缀。")

import random

def check_duplicate_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    string_dict = {}

    for index, line in enumerate(lines):
        string = line.strip()
        if string in string_dict:
            string_dict[string].append(index + 1)
        else:
            string_dict[string] = [index + 1]

    # 检查是否存在重复行
    duplicates_exist = False

    for string, line_numbers in string_dict.items():
        if len(line_numbers) > 1:
            duplicates_exist = True
            print(f'重复的字符串 "{string}" 在以下行中出现：{line_numbers}')

    if not duplicates_exist:
        print("文件中每一行都是唯一的，没有重复行")


# 读取txt文件内容
with open('filenames.txt', 'r') as file:
    lines = file.readlines()

# 打乱每一行内容的位置
random.shuffle(lines)

# 将打乱后的内容写入新的txt文件
with open('shuffled_file.txt', 'w') as file:
    file.writelines(lines)


check_duplicate_lines('shuffled_file.txt')