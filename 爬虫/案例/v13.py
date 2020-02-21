from urllib import request,parse
from http import cookiejar


#创建cookijar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load("cookie.txt",ignore_discard=True,ignore_expires=True)
#生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#生成cookie的管理器
http_handler = request.HTTPHandler()
#创建http请求管理
https_handler = request.HTTPHandler()
#创建请求管理
opener = request.build_opener(http_handler,https_handler,cookie_handler)


def getHomePage():
    #此处的网址为登录成功的网址
    url = 'http://www.renren.com/971485656/newsfeed/photo'

    #如果已经执行了login函数，则opener自动已经包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()


    with open("v11.html","w") as f:
        f.write(html)
if __name__ == '__main__':

    getHomePage()
