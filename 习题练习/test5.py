"""var=1
while var==1:
    number=int(input("请输入一个数字："))
    #print("你输入的数字是:{0}".format(number))
    print("你输入的数字是",number)
print("再见")
"""
"""
#计算1—100之间偶数和的程序
i=0
j=0
for i in range(1,101):
    if i%2==0:
       j+=i
print("总和是%s"%j)
"""
"""
i=1
while i < 6:
    j=0
    while j<i:
        print("* ",end='')
        j+=1
    print("\n")
    i=i+1
"""
"""
i=1
while i<10:
    j=1
    while j<=i:
        print("{0}*{1}={2}".format((i),(j),(i*j)),end=" ")
        j+=1
    print("\n")
    i+=1
"""

"""
str='I love you 3000 times'
j=0
for i in str:
    if i.isdigit():
        j+=1
    else:
        continue
print(j)
"""
"""
str=input("请输入字符串：")
str1=""
str2=""
for i in (str[::2]):
    str1=str1+i
for j in (str[1::2]):
    str2=str2+j
str3=str1+str2
print(str3)
"""
"""
arr = []
def count():
    myStr = input("请输入只包含字母的字符串：")
    if myStr.isalpha():   #判断是否是字母
        newStr = myStr.lower()   #lower() 方法转换字符串中所有大写字符为小写。
        for string in newStr:
            arr.append(string)
        a = {}
        for i in arr:
            if arr.count(i) >= 1:
                a[i] = arr.count(i)   #将返回的次数给字典a
        print(a)
    else:
        print("输入的内容有误")
count()
"""
"""
str=input("请输入字符串")
str1=[]
for i in str:
    str1+=i
last=str1[-1]
str1.remove(last)
str1.insert(0,last)
print(str1)
"""

""""
num=[]
num=input("请输入奇数个数字")
move=len(num)//2
print(num[move])
"""

""""
num=int(input("请输入几个整数"))
length=num
arr=[]
i=0
while i<length:
    numb=int(input("").format(i+1))
    arr.append(numb)
    i+=1

for i in range(length):
    flag = 0
    for j in range(1,length):
        if arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            flag = 1
    if not flag:
        break
print(arr)
"""
"""
arr = []
length = int(input("请输入列表的总个数:"))
i = 0
while i < length:
   element =  input("输入第%d个元素:"%(i+1))
   arr.append(element)
   i+=1
# 列表转为集合
newList = set(arr)
print(newList)
"""
"""
def stands(s):
    t=[]
    t=s.lower()
    t=t.capitalize()
    print(t)
    return  t

print(list(map(stands,['ANsan','NJSAnjjk'])))
"""
"""
file_name=input("请输入文件名称")
def file_write(file_name):
   f = open(file_name,"w")
   print("请输入内容（按:w结束退出）")
   while True:
       write_something=input()
       if write_something != ":w":
           f.write("%s\n" %write_something)
       else:
           break
   f.close()
file_write(file_name)
"""
"""

file1=input("请输入第一个文件名")
file2=input("请输入第二个文件名")
def file_compare(file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    count=0 #统计行数
    differ=[] #统计不同的数量
    for line1 in f1:
        line2=f2.readline()
        count+=1
        if line1 != line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ
differ=file_compare(file1,file2)
if len(differ) == 0:
    print("两个文件相同")
else:
    print("两个文件有{0}出不同".format(len(differ)))
    for i in differ:
        print("第{0}行不同".format(i))
"""
"""
class Car:
    def __init__(self,color):
        self.color=color
    def toot(self):
        print("%s的车在鸣笛"%(self.color))
car=Car("彩色")
car.toot()
"""
"""
#定义表示战士敌人的类
class Person:
    def __init__(self,name):
        #姓名
       self.name=name
        #血量
       self.blood=100
    #给弹夹安装子弹
    def install_bullet(self,clip,bullet): #clip表示弹夹  bullet表示子弹
        #弹夹放置子弹
        clip.save_bullets(bullet)

#定义一个表示弹夹的类
class Clip:
    def __int__(self,capacity): #capacity表示弹夹容量
        self.capacity=capacity
        #子弹数量
        self.current_list=[]
    #安装子弹
    def save_bullets(self,bullet):
        #当前子弹数量小于最大容量
        if len(self.current_list)<self.capcaity:
            self.current_list.append(bullet)
    def __str__(self):
        return "弹夹当前的子弹数量是"+str(len(self.current_list)) + "/" +  str (self.capcaity)

#定义一个子弹类型
class Bullet:
    pass

#创建一个战士
soldier=Person("老王")
#创建一个弹夹
clip=Clip()
print(clip)
#添加5颗子弹
i=0
while i < 5 :
    #创建一个子弹
    bullet=Bullet()
    #战士安装子弹
    soldier.install_bullet(clip,bullet)
    i+=1
#输出当前弹夹中子弹的数量
print(clip)
"""
"""
class Circle:

    def __init__(self,radio):
        self.radio=radio
    def zhouchang(self):
        return 3 * 2 * self.radio
    def mianji(self):
        return 3 * self.radio * self.radio

radio=int(input("请输入半径"))
circle=Circle(radio)
print(circle.zhouchang())
print(circle.mianji())
"""


