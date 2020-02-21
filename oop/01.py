#定义一个学生类，来形容学生
class Student:
   #一个空类 ，pass代表直接跳过
   #此处pass必须有
    pass

#定义一个对象
lhq=Student()

#定义一个类，用来描述python的学生
class PythonStudent():
    name=None
    age=18
    course="Python"
    def doHomework(self):
        print("我在做作业")
        return None

qq=PythonStudent()
print(qq.age)
print(qq.course)
qq.doHomework()
print(PythonStudent.__dict__)