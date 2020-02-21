from urllib import request

if __name__ == '__main__':
   #此处的网址为登录成功的页面，换一台电脑登录这个页面是进不去的，如果加上cookie就可以登录进去
    url = 'http://www.renren.com/971485656/newsfeed/photo'
    #加入cookie的请求头
    headers ={
        "Cookie" : "anonymid=jy2r2yfo4787vn; depovince=HEN; jebecookies=ed5bdcf4-89af-4cde-b0c8-6d320b3782ec|||||; _r01_=1; JSESSIONID=abcW8yAnch6eggIWJYVVw; ick_login=a6337fa9-01cc-4146-a76b-4ec919b8f73e; t=dd66a5453626d815d5b5a59a6975766a6; societyguester=dd66a5453626d815d5b5a59a6975766a6; id=971485656; xnsid=1035697e; ver=7.0; loginfrom=null; jebe_key=ac15d1f6-0be7-4a45-bc2c-345120852c33%7Ce73a792a6bd2e095e20c2de70ff506bf%7C1563096167081%7C1%7C1563096165476; jebe_key=ac15d1f6-0be7-4a45-bc2c-345120852c33%7Ce73a792a6bd2e095e20c2de70ff506bf%7C1563096167081%7C1%7C1563096165479; wp_fold=0"

    }
    req = request.Request(url ,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    #将爬取到的网页打印到一个文件中
    with open ("req.html", "w") as f :
        f.write(html)