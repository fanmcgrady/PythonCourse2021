class User:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("hello, {}".format(self.name))

class Teacher(User):
    def say(self):
        print("hello Teacher, {}".format(self.name))

user = User("zhangsan")
user.say()

teacher = Teacher("fangzhiyang")
teacher.say()

# print(dir(User))


# print(type(user))
# print(User.__name__)
# print(User.__dict__)
# print(User.__module__)
# print(User.__bases__)