"""
利用parse模块模拟post请求
分析百度翻译
分析步骤
1.打开F12
2.尝试输入单词girl，发现每敲一个字母后边都有请求
3.请求输入地址是https://fanyi.baidu.com/sug
4.利用NetWork-All-Headers 查看发现FormData的值是 kw：girl
"""

from urllib import parse,request
import json


# 2. 表示忽略未经核实的SSL证书认证


"""
大致流程
  1.利用data构造内容，然后urlopen打开
  2.返回一个json格式的结果
  3.结果应该就是girl的翻译结果
"""
#基础url
baseurl = 'https://fanyi.baidu.com/sug/'
#存放用来模拟form的数据一定是dict格式
data = {
    'kw' : 'girl'
}

#需要使用parse模块对data进行编码
#此处data得到的格式是str，因为下边reauest.urlopen需要的是bytes格式，所以需要编码
data = parse.urlencode(data).encode()

#我们需要构造一个请求头，请求头部应该至少包含转入的数据的长度
#request要求传入的请求头是一个dict格式

headers = {
    #因为post至少应该包含content-length字段
    "Content-Length" : len(data)
}

#有了headers  data  url  就可以尝试发出请求
rsp = request.urlopen(baseurl,data=data)
json_data = rsp.read().decode('utf-8')

#把json字符串转换成字典
json_data = json.loads(json_data)
print(json_data)
