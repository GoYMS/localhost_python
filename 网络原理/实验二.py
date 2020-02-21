


"""
1.
  判断素数
def prime(n):
   if n<2:
       print("False")
   if n==2:
       print("True")
   for i in range(2,n):
       if n%i==0:
           print("False")
           break

   else:
       print("True")

if __name__ == '__main__':
    n = int(input('请输入一个正整数:'))
    prime(n)
"""

"""
2.
   #孪生素数


def prime(n):
   if n<2:
       return False
   if n==2:
       return True
   for i in range(2,n):
       if n%i==0:
           return False
           break

   else:
       return True

if __name__ == '__main__':
    for i in range(1,100):
        if prime(i) == True and prime(i+2) == True:
            print("{0}和{1}是孪生素数".format(i,i+2))

"""

"""
3.摄氏温度和华氏温度的转换
"""
def change(c):
   F = c *1.8 + 32
   print("转换成摄氏温度为：{0}".format(F))

def change2(f):
    C = (f-32)/1.8
    print("转换成华氏温度为：{0}".format(C))
if __name__ == '__main__':
    i = int(input("请选择摄氏温度(1)或华氏温度(2)："))
    if i == 1:
        c = float(input("请输入摄氏温度："))
        change(c)
    else:
        f = float(input("请输入华氏温度："))
        change2(f)
        






