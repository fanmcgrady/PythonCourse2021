# 代码 1：
try:
    fp = open(r'd:\test.txt')
    print('Hello world!', file=fp)
finally:
    fp.close()

# 代码 2：
try:
    fp = open(r'd:\test.txt', 'a+')
    print('Hello world!', file=fp)
finally:
    fp.close()
