#在函数odd中，yield负责返回
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 2")
    yield 2

#odd()是调用生成器
g=odd()
one=next(odd())
print(one)
two=next(odd())
print(two)
three=next(odd())
print(three)