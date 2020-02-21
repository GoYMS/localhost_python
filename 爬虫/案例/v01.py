"""
使用urllib.request请求一个网页内容，并把内容打印出来
"""
from urllib import request

if __name__ == '__main__':
    url = "http://www.nyist.edu.cn/"
    #urlopen作用：打开相应的url并把网页作为返回
    rsp = request.urlopen(url)
    #把返回结果读取出来，读取出来得内容类型为bytes
    html = rsp.read()

    #需要将返回内容进行解码才能看懂

    html = html.decode()

    print(html)