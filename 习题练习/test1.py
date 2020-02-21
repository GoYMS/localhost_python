
# 斐波那契数列
'''
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10))
'''


#九九乘法表
'''
for i in range(1,10):
   for j in range(1,i+1):
     print("{0}*{1}={2}".format(i,j,i*j), end=" ")
   print()
'''
"""
name=input("请输入你的姓名：")
print("你好:{}".format(name))
"""


"""
i=input("请输入一个整数:") #input默认输入的都是字符串，
if i.isdigit():  #判断输入的是否全是数字
    i=int(i)
    if(1<=i<=100):
        print("你好看")
    else:
        print("你真丑")
else:
    print("你真丑")
"""


#写一个程序，判定给定的年份是否是闰年（闰年的定义是能够被四整除的是闰年）
"""
year=input("请输入一个年份:")
if year.isdigit():
    year=int(year)
    if(year % 4 == 0):
        print(str(year)+"是闰年")
    else:
        print(str(year)+"不是闰年")
else:
    print("你输入的不是年份，请重新输入")
"""



#题目：给用户一次机会，猜想程序随机生成的数字，每次猜想后会提示太大或太小，
# 机会用尽后提示机会用完了
"""
import random    #导入random函数包（个人理解）
srcret=random.randint(1,100) #利用random函数随机生成一个数字

times=3
while times:
    num = input("请输入你想猜想的数字：")
    if(num.isdigit()):  #判断输入的数字是否全是数字
       number= int(num)
       if(number==srcret):
            print("你真厉害啊！！")
            break
       elif(number > srcret):
            print("你想的太大了")
            times=times-1
       else:
            print("你想的太小了！")
            times=times-1

    else:
        print("兄弟看清楚题目")
print("三次机会全部用完！谢谢参与！")
"""


#题目：写一个程序，打印出0—100的所有奇数

"""
ls=range(0,101)
for i in ls:
    if (i % 2 !=0):
        print(i)
"""

#题目：爱因斯坦曾出过这样一道数学题：有一条长阶梯，若每步跨2阶，最后剩下1阶；若每步跨3阶，
# 最后剩下2阶；若每步跨5阶，最后剩下4阶。若每步跨6阶，则最后剩下5阶。只有每步跨7阶，才刚好跨完。
#求至少有多少台阶
"""
x=0
while x<1000 :
    if(x % 2==1)\
      and (x % 3==2)\
      and (x % 5==4)\
      and (x % 6==5)\
      and (x % 7==0):
      print(x)  #上边的 \ 代表的是可以换行
      break
    else :
        x+=1
"""

#假设有xyz三个变量，如何将三个变量的值迅速转换
"""
x=1
y=2
z=3
x,y,z=z,x,y
print(x)
print(y)
print(z)
"""

#   设计一个用户验证密码的程序，用户只有三次机会输入错误，不过用户输入“*”则不计算在内
"""
password="abc123"
times=3
while times:
    password_input=input("请输入你的密码：")
    if '*' in password_input:
        print("密码中不能包含*号，这次不算")
    else:
        if password_input ==password :
            print("恭喜你密码正确")
            break
        else:
            print("对不起密码有误")
            times-=1
print("三次机会全部用完")
"""

#打印一个实心的三角形
"""
*
* *
* * *
* * * * 
* * * * *

for i in range(0,5):
    for j in range(i+1):
        print("* ", end="")
    print()
"""
#打印一个空心三角
"""
*
* *
*   *
*     *
* * * * *

for i in range(0,5):
    for j in range(i+1):
        if i==4:
          print("* ", end="")
          continue
        if j==0 or j==i:
            print("* ", end ="")
        else:
            print(" ",end=" ")
    print()

"""
#打印一个倒立三角
"""
for i in range(0,5):
    for i in range(5-i):
        print("* ",end="")
    print()
"""
#打印一个空心倒立三角
"""
* * * * * 
*      *
*     *
*    *
*   *
*  *
*
 for  i in range(0,5):
    for j in range(5-i):
        if i==0:
            print("* ",end="")
            continue
        if j==0 or j==5-i-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
"""
#打印一个正三角
"""
for i in range(0,6):
    for j in range(0,6-i):
        print(" ",end="")
    for m in range(0,i+1):
        print("* ", end ="")
    print()
"""

#求100-999之前的水仙花数（一个数等于其各位数字的立方和)
for i in  range(100,1000):
    temp=list(str(i))
    a=temp[0]
    b=temp[1]
    c=temp[2]
    if i==a*a*a+b*b*b+c*c*c:
        print(i)





