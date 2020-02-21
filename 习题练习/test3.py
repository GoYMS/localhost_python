"""
习题一：

定义一个类，
姓名，年龄，成绩（语文，数学，英语）
获取年龄姓名
返回成绩中的最高的

class Student(object):
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
    def get__name(self):
        return self.name
    def get__age(self):
        return self.age
    def get__scores(self):
        return max(self.scores)
A=Student("yms",18,[100,200,300])
print(A.get__age())
print(A.get__scores())
"""
"""
习题二：

定义一个字典类: DictClass,完成如功能
      1.删除某个key del _dict(key)
      2.判断某个键是否在字典里，如果在返回键对应的值，不在则返回'not found get dict)'
      3.返回键组成的列表返回类型: list get_ key()
      4.合并字典，并且返回合并后字典的values组成的列表，返回类型list update dict()

class DictClass(object):
    def __init__(self,dict):
        self.dict=dict
    def del__dict(self,key):
        if key not in self.dict.keys():
            return "不存在"
        else:
            self.dict.pop(key)

            return print("已经删除{0}".format(key))
    def get__dic(self,key):
        if key not in self.dict.keys():
            return "no  found"
        else:
            return self.dict[key]
    def get__key(self,key):
        return self.dict.keys()
    def update__key(self,dict2):
       self.dict= dict(self.dict,**dict2) # 加上**代表两个dict进行复制
        retun self.dict
A=DictClass({'a':1,'b':2})
print(A.get__dic('a'))
"""

"""
习题三：
   定义一一个列表的操作类Listinfo
包括的方法
1.列表元素添加: add key()
2.列表元素取值: get key()
3.列表合并:  update_ list(list)
4.删除并且返回最后一个元素: del key()


class  Listinfo(object):
    def __init__(self,list_val):
        self.list=list_val
    def add_key(self,key_name):
        self.list.append(key_name)
        print(self.list)
        return "OK"
    def get_key(self,index):
        if index >0 and index < len(self.list):
            return self.list[index]
        else:
            return "对不起  输入的数字不在范围之内"
    def update_key(self,new_list):
        list2=self.list + new_list
        return list2
    def del_key(self):
        if len(self.list)>=0:
            return self.list.pop(-1)
        else:
            return  "你的列表是空的！"


A=Listinfo([1,2,3,4,5,6])
#print(A.add_key(7))
#print(A.get_key(3))
#print(A.update_key([7,8,9]))
print(A.del_key())
"""
"""
习题四：
定义一个集合的操作类
包括的方法
1.集合元素添加: add_ setinfp()
2.集合的交集: get jintersec.on()
3.集合的并集:getunion()
4.集合的差集，del_difference()

class  set (object):
    def __init__(self,my_set):
        self.set=my_set
    def add_set(self,key):
        self.set.add(key)
        return self.set
    def get_intersection(self,set2):
        return self.set & set2
    def get_union(self,set3):
        return self.set | set3
    def del_difference(self,set4):
        return self.set - set4
A=set({1,2,3,4})
#print(A.add_set(5))
#print(A.get_intersection({2,3}))
#print(A.get_union({5,6,7}))
print(A.del_difference({1,2,3}))
"""
"""

习题五：
   定义一个门票系统
    1.门票的原价是100
    2.当周末的时候门票涨20%
    3.小孩子半票
    4.计算两个成人和一个小孩的平日票价
    

class Ticket():
    def __init__(self,weekend=False,child=False):
        self.price=100
        if weekend:
            self.weekendmoney=1.2
        else:
            self.weekendmoney=1
        if child:
            self.childmoney=0.5
        else:
            self.childmoney=1

    def all(self,num):
        return self.price* self.weekendmoney * self.childmoney * num
child=Ticket(child=True)
people=Ticket()
print(child.all(1)+people.all(2))
"""

"""
习题六：
游戏编程按一下要求定义一
个乌龟类和鱼
类并尝试编程

●假设游戏场景为范围(x.y)
为0 <= x <= 10, 0 <= y <= 10

游戏生成1只乌龟和10条鱼他们的移动方向均随机

●乌龟的最大移动能力是2(乌龟可以随机选择移动是1还是2)
鱼的最大移动能力是1●当移动到场景边缘，自动向反方向移动

乌龟初始化体力为100(上限)
乌龟每移动一次，体力消耗1

●当乌龟和鱼重叠，乌龟吃掉鱼, 乌龟体力增加20.鱼不计算体力

●当乌龟体力值为0或者
鱼的数量为0时，游戏结束

import random as r

class  Turtle(object):
      def __init__(self):
          self.power=100 # 定义一个乌龟的能量
           #初始化乌龟的位置
          self.x=r.randint(1,10)
          self.y=r.randint(1,10)
      def move(self):
        #乌龟最新移动的位置
           new_x=r.choice([1,2,-1,-2])+self.x
           new_y=r.choice([1,2,-1,-2])+self.y
        #判断乌龟的移动是否超出了边界
           if new_x<0:
               self.x=0-(new_x-0)
           elif new_x>10:
               self.x=10-(new_x-10)
           else:
               self.x= new_x

           if new_y < 0:
               self.y = 0 - (new_y - 0)
           elif new_y > 10:
               self.y = 10 - (new_y - 10)
           else:
               self.y = new_y

           self.power -= 1
           return (self.x,self.y)
      def eat(self):
          self.power +=20
          if self.power>=100:
              self.power=100
class Fish(object):
      def __init__(self):
          self.x=r.randint(0,10)
          self.y=r.randint(0,10)
      def move(self):
          new_x = r.choice([1,-1]) + self.x
          new_y = r.choice([1,-1]) + self.y

          if new_x < 0:
              self.x = 0 - (new_x - 0)
          elif new_x > 10:
              self.x = 10 - (new_x - 10)
          else:
              self.x = new_x

          if new_y < 0:
              self.y = 0 - (new_y - 0)
          elif new_y > 10:
              self.y = 10 - (new_y - 10)
          else:
              self.y = new_y


              return (self.x, self.y)


turtle=Turtle()
fish=[]
for i in range(0,10):
    new_fish=Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼被吃完，游戏结束")
        break
    if not turtle.power:
        print("乌龟体力耗尽，游戏结束")
        break

    pos = turtle.move()
    for each_fish in fish[:]:
        if each_fish.move()==pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")
"""
"""
定义一个点类和一个直线类，使用类获取两点之间构成直线的距离
"""

import math

class  Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class Line(object):
    def __init__(self,p1,p2):
        self.x=p1.get_x()-p2.get_x()
        self.y = p1.get_y() - p2.get_y()

        self.len=math.sqrt(self.x*self.x+self.y*self.y)
    def get_len(self):
        return self.len

p1=Point(2,3)
p2=Point(5,7)
line=Line(p1,p2)
print(line.get_len())