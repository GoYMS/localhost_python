import requests

url = 'http://www.baidu.com'

#两种请求方式
#第一种：使用get请求

rsq = requests.get(url)
print(rsq.text)


#第二种：使用request请求,第一个参数是请求方式

rsp = requests.request("get",url)
print(rsp.text)
