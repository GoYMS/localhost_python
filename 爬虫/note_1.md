#爬虫
      -参考资料
         -python网络数据采集     -图灵工业出版
         -精通Python爬虫框架Scrapy   -人民邮电出版社
         [python3网络爬虫]  http://blog.csdn.net/c406495762/article/details/72858983
         [Scrapy官方教程] http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html
         
#前提知识
      -url
      -http协议
      -web前端, html css js
      -ajax
      -re ,xpath
      -xml
#爬虫简介
       定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），
             是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。
             另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
       
       两大特征：
            -能按作者要求下载数据或者内容
            -能自动在网络上流窜
       三大步骤； 
            1.下载网页
            2.提取正取的信息
            3.根据一定规则自动跳转到另外的网页上执行上述两步内容
            
       爬虫分类
           -通用爬虫
           -专业爬虫（聚焦爬虫）
           
       Python网络包简介
           -Python2.X ：urllib ,urllib2 ,urllib3,httplib ,httplib2.requests
           -Python3.x :  urllib ,urllib3,httplib2 ,requests
           -python2中经常使用的：urllib和urllib2配合使用，或者requests
           python3中经常使用的：urllib ,requests
#urllib
       -包含模块
           -urllib.request:打开和读取urls
           -urllib.error :包含urllib.request产生的常见的错误，使用try捕捉
           -urllib.parse :包含解析url的方法
           -urllib.robotparse:解析robots.txt文件
           案例v01
           
#网页编码问题解决
       -chardet 可以自动检测页面文件的编码格式，但是可能有误
       -需要安装  conda install chardet
       案例V02
       
#request.data 的使用
       -访问网络的两种方法
          -get
              利用参数给服务器传递信息
              参数为dict，然后利用parse编码
           案例 v03   
          -post   
              一般向服务器传递参数使用
              post是把信息自动加密处理
              我们如果想使用post信息，需要用到data参数
              使用post，意味着Http的请求头可能需要更改：
                   Content-Type :application/x-www/form-urlencode
                   Content-Length :数据长度
                   简而言之就是一旦更改请求方法，请注意其他请求头部信息相适应
              - urllib.parse.urlencode 可以将字符串自动转换成上面的
          案例v04      
              -为了更多的设置请求信息，单纯的通过urlopen函数已经不太好用了
              需要利用request.Request类
          案例v05  

#urllib.error
         -URLError产生的原因
            -没网
            -服务器链接失败
            -找不到指定服务器
            -是OSError的子类
         案例v06
         -HTTPError ,是URLError的一个子类
         案例v07
         
         两者的区别：
              HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上，则会引发HTTPError
              URLError对应的是一般是网络出现问题，包括URL问题
              关系区别 ：OSError - URLError -HTTPError
              
#UserAgent 
        把自己伪装一个浏览器
        UserAgent ；用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者的身份
        常见的UA值 ：使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
                浏览器访问抓包方法获取User-Agent的值
                     1.打开一个网址
                     2.按F12
                     3.点击网络
                     4.选择一行，在其右边最下有个User-Agent的值，可以直接使用
                     5.见图片01
        设置UA可以通过两种方式
         -heads
         -add_header
         案例v08
         
#ProxyHandler（代理服务器）
       -使用代理IP ,是爬虫的常用手段
       -获取代理服务器的地址
             -www.xicidaili.com
             -www.goubanjia.com
       -代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多很多
       -基本使用步骤
           1.设置代理地址
           2.创建ProxyHandler
           3.创建Opener
           4.安装Opener
       案例v09
#cookie &  session
       -由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
       -cookie是发放给用户，（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息
        
         
       -cookie和session的区别
          -存放位置不同
          -cookie不安全
          -session会保存在服务器上一定时间，会过期
          -单个cookie保存数据不超过4k
       -session的存放位置
           -存在服务器端
           -一般情况下，session是放在内存中或者数据库中
           -没有cookie登录，案例v10，可见如果没有使用cookie，显示的网页为未登录状态
       -使用cookie登录
            1.直接把cookie复制下来，然后手动放入请求头(请求头也是按F12进行查找)，
            案例v10
            2.http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
                   -CookieJar
                      -管理存储cookie.向传出的http请求添加cookie
                      -cookie存储在内存中，CookieJar实例回收后cookie将消失
                   -FileCookieJar（filename，delayload=None，policy=None）：
                       -使用文件管理cookie
                       -filename是保存在cookie的文件
                   -MozillaCookieJar（filename，delayload=None，policy=None）
                      -创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
                   -LwpCookieJar（filename，delayload=None，policy=None）
                      -创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
                   -他们的关系是: CookieJar-->FileCookieJar--> MozillaCookieJar &  LwpCookieJar
              自动使用cookie登录，大致流程是
                 1.打开登录页面后自动通过用户名和密码登录
                 2.自动提取反馈回来的cookie
                 3.利用提取的cookie登录隐私页面
              利用cookiejar访问人人网  案例v11
              案例v11代码解析
                handler是Handler的实例，用来处理复杂请求，常见参数见案例代码
                    #生成cookie的管理器
                    cookie_handler = request.HTTPCookieProcessor(cookie)
                    #生成cookie的管理器
                    http_handler = request.HTTPHandler()
                    #创建http请求管理
                    https_handler = request.HTTPHandler()
                创立handler后，使用opener打开，打开后相应的业务由相应的handler处理
                
              cookie作为一个变量，打印出来，
                  cookie的属性
                     name：名称
                     value ：值
                     domain ：可以访问次cookie的域名
                     path ：可以发现cookie的页面路径
                     expires：过期时间
                     size ：大小
                     Http字段
              
            cookie的保存 -FileCookieJar  案例v12
            cookie的读取 -案例v13
            
         
#SSL
       -SSL证书就是指遵守ssl安全套阶层协议的服务器数字证书（SercureSocketLayer）
       -美国网景公司开发
       -遇到不信任的SSL证书，需要单独处理，案例v14
       
#js加密
       -有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是取md5）
       -经过加密，传输的就是密文，但是
       -加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
       -通过阅读加密算法，就可以模拟出加密过程，从而达到破解
       过程参考案例v15
   
#ajax
       -异步请求
       -一定会有url，请求方法，可能有数据
       -一般使用json格式
       -案例：爬取豆瓣电影   案例v16
       
       
       
#第二种模块       
#Requests模块-献给人类 
                   -继承了urllib的所有特征，底层使用的是urllib3
                   -开源地址；https://github.com/requests/requests
                   -中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
                   -安装：cmd中输入 pip install requests
    -get请求
                   -requests.get(url)
                   -requests.request("get",url)
                   -可以带有headers(请求头)和parmas(url后边的参数)参数
                   案例v17
          -get返回内容
             案例v18
        
    -post请求
                rsp = requests.post(url,data=data)
                data,headers要求dict类型，也就是说不需要编码
            案例v19

           
              
    -proxy(代理)
                proxies={
                  "http":"address of proxy"
                  "https":"address of proxy"
                }            
                 rsp = requests.get("get"."http://www.xxxx",proxies=proxies)    
             -代理有可能出错，如果使用人数多，考虑安全问题，可能被强行关闭
         
    -用户验证
            代理验证
                     #可能需要使用HTTP basic Auth ：可以这样
                     #格式为 用户名：密码@代理地址：端口地址
                     proxy = {"http":"china:123456@192.168.2.123:4444"}
                     rsp = request.get("http://www.baidu.com",proxies=proxy)
    web客户端验证
            如果遇到web客户端验证，需要添加auth = (用户名，密码)
            auth = ("text1","123456") #授权信息
            rsp = requests.get("http://www.baidu.com",auth=auth)         
            
    cookie
        -requests可以自动处理cookies信息
                   
                    rsp = requests.get("http://xxxxx")
                    #如果对方服务器传送过来cookie信息，则可以通过反馈的cookie属性得到
                    #返回一个cookiejar实例
                    cookiejar = rsp.cookies
                    
                    #可以将cookiejar转换成字典
                    cookiedict = requests。untils.dict_from_cookiejar(cookiejar)
    session
         -跟服务器段session不是一个东西
         -模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开
         -能让我们跨请求时保持某些参数，比如在同一个session实例发出，所有请求之间保持cookie
                      #创建session对象，可以保持cookie值
                      ss = requests.session()
                      headers = {"User-Agent" :"xxxxx"}
                      data = {"name" ;"xxxxx"}
                      #此时由创建的session管理请求，负责发出请求
                      ss.post("http://www.baidu.com",data=data,headers=headers)
                      rsp=ss.get("ssssss")
    
    https请求验证ssl证书
             -参数verify负责表示是否需要验证ssl证书，默认是True
             -如果不需要验证ssl证书，则设置成False表示关闭
             
                    rsp = requests.get("http://www.baidu.com",verify=False)
                    #如果用verify=True访问12306，会报错，因为他的证书有问题
                    
                    

          
       