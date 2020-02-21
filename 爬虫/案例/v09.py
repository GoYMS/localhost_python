"""
使用代理访问百度
"""

from urllib import request,error

if __name__ == '__main__':

    url = "https://www.baidu.com"
    #1.设置代理地址
    proxy = {'http':'120.83.120.242'}
    #2.创建ProxyHandler
    proxyhandler = request.ProxyHandler(proxy)
    #3.创建Opener
    opener = request.build_opener(proxyhandler)
    #4.安装Opener
    request.install_opener(opener)

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)