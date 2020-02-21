import json

#此时的1student是个python格式
student={
    "name":"yangmingshuai",
    "age":18,
    "mobile" : 12456
}

print(type(student))
#将python格式转换成json格式
stu_json=json.dumps(student)
print(type(stu_json))
print("JSON对象{0}".format(stu_json))
