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
    """
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    """
    #此url需要从登录界面获取，获取步骤 ：查看源码，在登录源码中获取action对应的地址,见图片02
    url = 'http://www.renren.com/PLogin.do'

    #此键值需要从登录的form的两个对应input中提取name属性,也就是用户名和密码在源码中对应的属性名称，见图03
    data = {
        "email" : "15515819567",
        "password" :"220018"
    }
    #把数据进行编码
    data = parse.urlencode(data).encode()
    #创建一个请求对象
    req = request.Request(url,data=data)
    #使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    #此处的网址为登录成功的网址
    url = 'http://www.renren.com/971485656/newsfeed/photo'

    #如果已经执行了login函数，则opener自动已经包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()


    with open("v11.html","w") as f:
        f.write(html)
if __name__ == '__main__':
    login()
    getHomePage()
