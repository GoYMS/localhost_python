"""
登录开心网
利用cookie
免除ssl
步骤：
   寻找登录入口，查询登录页面的网址，账号和密码在代码中对应的name
   账号：loginemail
   密码：password
"""
from urllib import request,parse
from http import cookiejar
#创建cookijar的实例
cookie = cookiejar.CookieJar()
#生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#生成cookie的管理器
http_handler = request.HTTPHandler()
#创建http请求管理
https_handler = request.HTTPHandler()
#创建请求管理
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    url = 'https://security.kaixin001.com/login/login_post.php'
    data = {
        "loginemail":15515819567,
        "password" : 220018
    }
    # data为url后边的参数，参数在实际应用中的url格式不一样，所以需要利用parse.urlencode编码为正确的格式，
    data = parse.urlencode(data)
    #data需要为bytes类型
    req = request.Request(url,data=data.encode())
    #使用opener发起请求
    opener.open(req)

def gethome():
    url = 'http://www.kaixin001.com/home/?_profileuid=181868997#'

    rsp = opener.open(url)
    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    login()
    gethome()