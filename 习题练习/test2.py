#汉诺塔的递归实现
'''
def hano(n, a, b, c):
    if n == 1:
        print(a ,"-->",b)
        return None
    if n==2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        return None
    hano(n-1, a, c, b)
    print(a, "-->", c)
    hano(n-1, b, a, c)
a = "A"
b = "B"
c = "C"
n=10
hano(n, a, b, c)
'''

'''
a=[["yms","nan"],["lhq","nv"]]
for k,v in a:
    print(k, "--", v)
    '''
'''
a=[1,23,3]
b=[i*20 for i in a]
print(b)
'''
'''
#列表的嵌套
a=[i for i in range(1,10)]
print(a)
b=[j for j in range(100,400) if j % 100 == 0]
print(b)
c=[m+n for m in a for n in b ]
print(c)
d=[m+n for m in a for n in b if m+n <300]
print(d)
'''
s={1,2,3,4}
print(type(s))
s={1,1,2,2,3,3,4,5,6,8,8}
print(s)
j={i for i in s if i>4 }
print(j)