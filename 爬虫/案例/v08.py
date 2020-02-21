"""
访问一个网址
更改自己的UserAgent进行伪装
"""

#Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
from urllib import request,error

if __name__ == '__main__':
    url = "https://www.baidu.com"
    try:
        #第一种方法：使用head方法进行伪装UA
        #headers = {}
        #headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
        #req = request.Request(url,headers = headers)


        #第二种方法，使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0(WindowsNT 10.0;Win64; x64; rv:68.0)Gecko/20100101 Firefox/68.0")

        #正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)