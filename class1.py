import os
import shutil

folder = r"C:\Users\fanmc\OneDrive\09-杂项\2021-脚本语言程序设计"
if __name__ == '__main__':
    files = os.listdir(folder)
    index = 0
    for file in files:
        index += 1
        # 源文件
        src = os.path.join(folder, file)
        if os.path.isdir(src):
            continue

        if "2022" in file:
            new_file = file.replace("2022", "2021")
            # 目标文件
            dest = os.path.join(folder, new_file)
            # 修改文件名
            shutil.move(src, dest)
            print("处理文件：{}".format(file))