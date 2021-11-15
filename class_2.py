import re

str = """
你好，我的电话是028-8599999四川大学
"""
# result = re.findall('\d{3,4}-\d{6,8}$', str)
# result = re.findall('^\d{3,4}-\d{6,8}', str)
# result = re.findall('\d{3,4}-\d{6,8}$', str)
# result = re.findall('9*', str)
# result = re.findall('9+', str)
# result = re.findall('59?', str)
# result = re.findall('.', str)
# str = 'industry, industries'
# result = re.findall('industr(?:y|ies)', str)
# str = "Windows 3000"
# result = re.findall('Windows (?:95|2000)', str)
# print(result)
# result = re.findall('Windows (?=95|2000)', str)
# print(result)
# result = re.findall('Windows (?!95|2000)', str)
# print(result)
# str = "never"
# result = re.findall('[^a-z]', str)
# result = re.findall('er', str)
# str = "@@@hello world, scu"
#
# pattern = re.compile('(\w+)(\s)(?=\w+)')
# result = pattern.match(str)
# print("没找到" if result is None\
#           else result.group())
# result = pattern.search(str)
# print(result.group())

# str = '01-1abc,02-2xyz,03-9hgf'
# # '01-1abc' -> '01-产品编号：(1-abc)'
#
# result = re.sub('([0-9])([a-z]+)',
#                 r'产品编号：(\1-\2)',
#                 str)
# print(result)

str = """
以上所有岗位，工作地点：深圳南山区
根据不同级别，薪资水平不同。货真价实的安全界绝对大牛，
薪资可以更高。以上岗位是业务持续扩展而产生的新领域
里面的新岗位，个人在此的发展前景非常大，
欢迎大家投递！在FreeBuf发表过文章或漏洞盒子白帽子加分。
联系人：徐先生 电话0755-86670332  
联系人：张小姐 电话0755-86670379  
简历投递邮箱：xuwei@sangfor.com  
QQ：2746329146  
公司网址：http://www.sangfor.com.cn
"""
print(re.findall('联系人：.+', str))