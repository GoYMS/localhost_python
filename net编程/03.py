"""
Server端流程
          1.建立socket，socket是负责具体通信的一个实例
          2.绑定，为创建的socket指派固定的端口号和IP地址
          3.接受对方的访问
          4.给对方发送反馈，此步骤为非必须步骤
"""

#socket模块负责socket编程
import socket

#模拟服务器的函数
def serverFunc():

#     1.建立socket
#     socket.AF_INET:使用Ipv4协议族
#     socket.SOCK_DGRAM： 使用UDP通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#     2.绑定ip和port
#    ‘127.0.0.1’ ：这个IP地址代表的是机器本身
#     7852 :随手指定的端口号
#     地址是一个元组类型  (ip，port)
    addr=("192.168.125.1",10023)
    sock.bind(addr)

#     3.接受对方消息
#      等待方式为死等，没有其他可能性
#       recvfrom接受的返回值是一个tuple，前一项表示数据，后一项表示地址
#       参数的含义是缓冲区大小
    data , addr =  sock.recvfrom(500)
    print(data)
    print(type(data))
#      发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
#      decode默认参数是utf-8
    text = data.decode()
    print(type(text))
    print(text)


#      给对方回消息
    rsp = "NO NO NO"
#发送的消息需要编码成bytes格式
#默认是utf-8
    data = rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    while True:
        try:

            serverFunc()
        except Exception as e:
            print(e)
