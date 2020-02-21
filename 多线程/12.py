import threading

sum=0
loopSum=1000000
#创建锁
lock=threading.Lock()
def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        #上锁（申请锁）
        lock.acquire()
        sum += 1
        #释放锁
        lock.release()
def myMinu():
    global sum,loopSum
    for i in range(1,loopSum):
        #上锁（申请锁）
        lock.acquire()
        sum -= 1
        #释放锁
        lock.release()

if __name__ == '__main__':
    # 采用多线程运行
    print("Start===={0}".format(sum))
    # 开始执行多线程
    # 务必记着target后边跟的是函数名称，不是函数（也就是说不要带括号）
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())
    # 启动
    t1.start()
    t2.start()
    # 等待多线程完成
    t1.join()
    t2.join()

    print("End==={0}".format(sum))
