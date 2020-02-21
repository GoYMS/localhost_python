import threading
sum=0
loopSum=1000000

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        sum += 1
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1


if __name__ == '__main__':
    """
    正常运行
    myAdd()
    print(sum)
    myMinu()
    print(sum)
    """
    #采用多线程运行
    print("Start===={0}".format(sum))
    #开始执行多线程
    #务必记着target后边跟的是函数名称，不是函数（也就是说不要带括号）
    t1=threading.Thread(target=myAdd,args=())
    t2=threading.Thread(target=myMinu,args=())
    #启动
    t1.start()
    t2.start()
    #等待多线程完成
    t1.join()
    t2.join()

    print("End==={0}".format(sum))

