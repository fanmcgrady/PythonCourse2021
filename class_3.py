# eval方法调用
# a = 1
# b = 2
# python_code = 'print(a + b)'
#
# eval(python_code)

# exec方法调用
# code = """
# for i in range(10):
#     print(i)
# """
# file = open('data.csv')
# code = file.read()
# file.close()
# exec(code)

# compile方法调用
# ecode = compile('print(100 + 200)', '', 'eval')
# eval(ecode)
#
# code = """
# for i in range(5):
#     print(i)
# """
# ecode = compile(code, '', 'exec')
# exec(ecode)
import pandas as pd
import numpy as np

if __name__ == '__main__':
    # matrix = [['张三', '001', 10],
    #           ['李四', '001', 10],
    #           ['王五', '001', 10]]
    # matrix = []
    # 0、读数据
    # with open('data.csv') as fp:
    #     content = fp.readlines()
    #     for index, line in enumerate(content):
    #         if index == 0:
    #             continue
    #         # 去掉\n
    #         line = line.strip()
    #         # 拆分成3个元素
    #         items = line.split(",")
    #         items[2] = int(items[2])
    #         matrix.append(items)
    # print(matrix)

    matrix = pd.read_csv('data.csv')
    print(matrix)
    print(type(matrix))
    print(len(matrix))

    # 1、rank平均值
    # sum = 0
    # for m in matrix:
    #     sum += m[2]
    # print("rank平均值 = {}".format(sum/len(matrix)))
    rr = matrix['rank'].values
    average = np.average(rr)
    print("rank平均值 = {}".format(average))

    # 2、查询“李四”的排名
    # for m in matrix:
    #     if m[0] == '李四':
    #         print("李四的排名是{}".format(m[2]))
    #         break
    index = matrix['name'] == '李四'
    print(matrix.loc[index]['rank'])

    # 3、查询“003”的姓名
    # for m in matrix:
    #     if m[1] == '003':
    #         print('“003”的姓名是{}'.format(m[0]))
    #         break
    index = matrix['number'] == '003'
    print('“003”的姓名是{}'.format(matrix.loc[index]['name'].values))