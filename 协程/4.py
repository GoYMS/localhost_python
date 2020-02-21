def simple_coroutine():
    print('->start')
    x=yield
    print('->recived',x)

#主线程
sc=simple_coroutine()
print(1111)
next(sc) #预激
print(2222)
sc.send('zhexiao')

"""
粗略解释：
将函数simple_coroutine()赋给sc，输出1111，遇到next(sc)转到simple_coroutine()函数，然后输出'->start'，
遇到yield返回到print(2222)，再遇到sc.send('zhexiao')，将'zhexiao'转给X，最后输出 print('->recived',x)

"""