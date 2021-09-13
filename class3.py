'''
一、遍历如下遍历
'''
# astr = 'hello'
#
# for ch in astr:
#     print(ch)
#
# for index, ch in enumerate(astr):
#     print(astr[index])
#
# alist = [10, 20, 30]
# for item in alist:
#     print(item)
#
# atuple = ('bob', 'tom', 'alice')
# for item in atuple:
#     print(item)
#
# adict = {'name': 'john', 'age': 23}
# for key, value in adict.items():
#     print("{}->{}".format(key, value))

'''
二、字符串方法
'''
# py_str2 = '    Hello world!   '
# py_str2 = py_str2.lstrip()
# print(py_str2)
# py_str2 = py_str2.rstrip()
# print(py_str2)
# py_str.capitalize()
# py_str.title()
# py_str.center(50)
# py_str.center(50, '#')
# py_str.ljust(50, '*')
# py_str.rjust(50, '*')
# py_str.count('l')  # 统计l出现的次数
# py_str.count('lo')
# py_str.endswith('!')  # 以!结尾吗？
# py_str.endswith('d!')
# py_str.startswith('a')  # 以a开头吗？
# py_str.islower()  # 字母都是小写的？其他字符不考虑
# py_str.isupper()  # 字母都是大写的？其他字符不考虑
# '  hello\t    '.strip()  # 去除两端空白字符，常用
# '  hello\t    '.lstrip()
# '  hello\t    '.rstrip()
# 'how are you?'.split()
# 'hello.tar.gz'.split('.')
# '.'.join(['hello', 'tar', 'gz'])
# '-'.join(['hello', 'tar', 'gz'])

'''
三、列表方法
'''
# alist = [1, 2, 3, 'bob', 'alice']
# print(alist[2])
# print(alist[2:4])
# print(alist[2:])
# alist.append('hello')
# print(alist)
# alist.remove('hello')
# print(alist)
# alist.insert(3, 4)
# print(alist)
# b = alist.pop()
# print(alist)
# print(b)
# b = alist.pop(3)
# print(alist)
# print(b)
#
# list2 = [3, 5, 2, 1]
# list2.sort()
# print(list2)
# list2.reverse()
# print(list2)
#
# list3 = [3, 5, 2, 1, 1, 2]
# print(list3.count(2))
#
# list2.append(list3)
# print(list2)
# print(len(list2))
#
# list2.extend(list3)
# print(list2)
# print(len(list2))

'''
四、tuple方法
'''
# tuple一般不操作
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple1 = tuple1 + tuple2
# print(tuple1*3)

'''
五、dict方法
'''
# adict = dict()  # {}
# adict = dict(['ab', 'cd'])
# print(adict)
#
# bdict = dict([('name', 'bob'), ('age', 25)])
# print(bdict)
#
# edict = {}.fromkeys(['zhangsan', 'lisi', 'wangwu'], 11)
# print(edict)
#
# del edict['zhangsan']
# print(edict)
# edict.pop('wangwu')
# print(edict)
# bdict.clear()

'''
六、set用法
'''
# 集合相当于是无值的字典，所以也用{}表示
# myset = set('hhhhhhhellooooooo')
# print(len(myset))
# for ch in myset:
#     print(ch)
#
# aset = set('abc')
# bset = set('cde')
# # # aset & bset  # 交集
# print(aset.intersection(bset))
# # # aset | bset  # 并集
# print(aset.union(bset))
# # # aset - bset  # 差补
# print(aset.difference(bset))
# aset.add('new')
# print(aset)
# aset.update(['aaa', 'bbb'])
# print(aset)
#
# aset.remove('bbb')

'''
七、类型间互相转换
'''
# str -> list
# string = "hello"
# print(string)
# ll = list(string)
# print(ll)
#
# # list -> str
# ll2 = ['h', 'e', 'l', 'l', 'o']
# "hello"
#
# str2 = "".join(ll2)
# print(str2)
#
# # str -> tuple
# string = "hello"
# tt = tuple(string)
# print(tt)
#
# # tuple -> list
# ll3 = list(tt)
# print(ll3)

'''
八、列表实现斐波那契数列
'''
# fib = [0, 1]
#
# for index in range(2, 100):
#     fib.append(fib[index - 1] + fib[index - 2])
#
# print(fib)

'''
九、逐步实现列表解析
'''
# list2 = [i for i in range(100) if i % 2 == 0]
# print(list2)

# 10+5的结果放到列表中
# 	[10 + 5]
# 	# 10+5这个表达式计算10次
# 	[10 + 5 for i in range(10)]
# 	# 10+i的i来自于循环
# list2 =	[10 + i for i in range(10)]
# # 	[10 + i for i in range(1, 11)]
# # 	# 通过if过滤，满足if条件的才参与10+i的运算
# list3 = [10 + i for i in range(1, 11) if i % 2 == 1]
# # 	[10 + i for i in range(1, 11) if i % 2]
# # 	# 生成IP地址列表
# ips = ['192.168.1.%s' % i for i in range(1, 255)]
# print(ips)

'''
十、整理桌面小程序
'''
import os
import shutil

# 1、取出桌面全部文件列表
desktop = r"C:\Users\fanmc\Desktop"
files = os.listdir(desktop)

# 2、过滤一些不需要处理的文件
# 过滤
# 另一种写法
file_need_process = [file for file in files
                     if not os.path.isdir(os.path.join(desktop, file))
                     and not file.endswith(".lnk")
                     and not file.endswith(".ini")]

# 判断文件类型
types = set()
for file in file_need_process:
    ext = file[file.rfind(".") + 1:]
    types.add(ext)

# 3、根据后缀创建文件夹
for type in types:
    os.mkdir(os.path.join(desktop, type))

# 4、将文件移入文件夹
for file in file_need_process:
    ext = file[file.rfind(".") + 1:]
    src = os.path.join(desktop, file)
    dest = os.path.join(desktop,
                        os.path.join(ext, file))
    print("移动文件：{}->{}".format(src, dest))
    shutil.move(src, dest)