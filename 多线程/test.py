"""
利用time函数，生成两个函数
顺序调用
计算总的运行时间
"""
"""
import time
import _thread as thread


def loop1():
    #ctime 获得当前的时间
    print('Start loop 1 at :',time.ctime())
    time.sleep(4)
    print('End loop 1 at :',time.ctime())
def loop2():
    #ctime 获得当前的时间
    print('Start loop 2 at :',time.ctime())
    time.sleep(2)
    print('End loop 2 at :',time.ctime())

正常运行
def main():
    print("All start :",time.ctime())
    loop1()
    loop2()
    print("All end ;",time.ctime())


#多线程运行
def main():
    print("All start :",time.ctime())
    
    #启用多线程的意思是用多线程去执行某个函数
    #启用多线程的函数是start_new_thread
    #参数有两个，一个事需要运行的函数，第二个是函数的参数作为元祖使用，为空则使用空元祖
    #注意；如果函数只有一个参数，需要参数后边的有一个逗号
   
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print("All end ;",time.ctime())
#多线程运行
if __name__ == '__main__':
    main()
    
"""
#使用多线程去播放两个列表，一个是move，一个是music
import threading
import time
move_list=["复仇者联盟","英雄归来","不可描述的"]
music_list=["周杰伦","五月天","伍佰"]

def play():

        time.sleep(4)
        print("现在看的电影是1")
def play2():
        print("现在收听的是2")
        time.sleep(3)

def thread_run():
    t1=threading.Thread(target=play(),args=())
    t2=threading.Thread(target=play2(),args=())
    t1.start()
    t2.start()

if __name__ == '__main__':
    thread_run()