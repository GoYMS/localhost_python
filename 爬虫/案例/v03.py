"""
掌握对url进行参数编码的方法
需要使用parse模块
"""
from urllib import request,parse

if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")

    #要想使用data，需要使用字典结构

    qs = {
        "wd":wd
    }

    #转化url编码
    qs = parse.urlencode(qs)
    print(qs)
    #将两段接为一起，一个完整的url
    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)

    html = rsp.read()

    html = html.decode()
    print(html)
