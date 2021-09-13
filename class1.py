import os
import shutil

folder = r"C:\Users\fanmc\Desktop\新建文件夹"
if __name__ == '__main__':
    files = class1.listdir(folder)
    index = 0
    for file in files:
        index += 1
        # 源文件
        src = class1.path.join(folder, file)
        # 目标文件
        dest = class1.path.join(folder, "{}、{}".format(index, file))
        # 修改文件名
        shutil.move(src, dest)
        print("处理文件：{}".format(file))