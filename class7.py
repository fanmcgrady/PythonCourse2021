# try:
#     a = 100 + '111'
# except:
#     print("程序出错！")
#
# try:
#     a = 100 + '111'
# except (TypeError, ZeroDivisionError) as error:
#     print("发生TypeError！")
# except TimeoutError:
#     pass
#
# try:
#     a = 100 + '111'
# except TypeError as error:
#     print(error)
#     print("程序出错！")
# class UserException(Exception):
#     def __init__(self, str):
#         self.str = str
#
# raise UserException("Hello Exception")
# import sys
#
# try:
#     a = 100 / 0
# except:
#     print(sys.exc_info())

# import Test
# Test.hello_world()

# from Test import hello_world
# hello_world()

# import Test as tt
# tt.hello_world()
import ML.CaptchaSequence as cs