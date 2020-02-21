"""
爬取百度贴吧，张继科吧
1.张继科主页网址 ：https://tieba.baidu.com/f?ie=utf-8&kw=张继科&fr=search
2.就去之后有很多页
      第一页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=0
      第二页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=50
      第三页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
      第四页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
      第五页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=200
3.由上面网址可以找到规律，每一页只有最后的数字不同，且数字应该是（页数-1）*50
解决方法：
1.准备构建参数字典
  字典包括三部分  kw  ie  pn
2.使用parse构建完整url
3.使用for循环下载
"""
from urllib import request,parse

if __name__ == '__main__':
    #准备构建参数字典
   qs = {
       "kw" : "张继科",
       "ie" : "utf-8",
       "pn" : 0
   }
    #构建url
   urls = []
   baseurl = "https://tieba.baidu.com/f?"
   for i in range(2):
       pn = i*50
       qs['pn'] = str(pn)
       #把qs编码后的和基础url进行拼接，形成完整的url
       urls.append(baseurl + parse.urlencode(qs))

   #使用for循环下载
   i = 0
   for url in urls:
       rsp = request.urlopen(url)
       html = rsp.read().decode()
       print(url)
       print(html)
       i += 1
       #将得到的页面打印到一个单独的HTML文件中
       with open("t01({}).html".format(i), "w",encoding="utf-8") as f:
           f.write(html)