"""
-Client端流程
          1.建立通信的socket
          2.发送内容到指定服务器
          3.接受服务器给定的反馈内容

"""
import socket

def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text="I LOVE YOU"

    #发送的数据必须是bytes格式
    data = text.encode()
    #发送
    sock.sendto(data, ("192.168.125.1",10023))
    #接受反馈

    data , addr  = sock.recvfrom(200)
    #解码
    data2 = data.decode()
    print(data2)

if __name__ == '__main__':
    clientFunc()