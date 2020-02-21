import socket


def tcp_srv():
    # 1.建立socket负责具体通信，这个socket其实只负责接收对方的请求，真正通信的是链接后
    # 需要用到两个参数
    # AF_INET:含义同udp一致
    # SOCK_STREAM：表明是使用的tcp进行通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.绑定端口和地址
    #此地址信息是一个元组类型内容，元组分两部分，第一部分为字符串，代表ip，第二部分为端口
    addr = ("192.168.125.1",10023)
    sock.bind(addr)
    #3.监听接入的访问socket
    sock.listen()

    while True:
        # 4.接受访问的socket,可以理解成接受访问即建立了一个通信的链接通路
        # accept返回的元组第一个元素赋给skt，第二个赋给addr
        skt , addr = sock.accept()
        #5.接受对方的发送内容，利用接收到的socket接受内容
        # 500代表接收的缓冲区
        msg  = skt.recv(500)
        #接收到的是bytes格式内容
        #想要得到str格式的，需要进行解码
        test = msg.decode()
        print(test)
        #如果有必要，要给对方回复
        rst = "收到了"
        skt.send(rst.encode())
        #关闭链接通路

if __name__ == '__main__':
    tcp_srv()