"""
利用request下载页面
使用chardet自动检测页面编码
"""
import chardet
from urllib import request


if __name__ == '__main__':
    url="http://www.nyist.edu.cn/"
    rsp = request.urlopen(url)
    html = rsp.read()

    #利用chardet自动检测，检测到的结果赋给cs
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    #cs使用get得到所检测出来得编码格式：encoding,如果检测不到，就直接使用utf-8编码
    #使用get取值保证不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)



