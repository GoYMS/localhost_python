#页面解析和数据提取
- 结构数据：先有数据，再谈数据
        -JSON文件
              -JSON Path
              -转换成Python类型进行操作（json类）
        -XML文件
              -转换成python类型(xml to dict)
              -Xpath
              -CSS选择器
              -正则 
- 非结构化数据：先有数据，再谈结构
        -文本
        -电话号码
        -邮箱地址
              -通常处理此类数据，使用正则表达式
        -html文件
              -正则
              -Xpath
              -CSS选择器
#正则表达式
- 一套规则，可以在字符串文本中进行搜查替换等
          案例v20 re的基本使用步骤
          案例v21 match的基本使用
- 正则常用方法
        -match: 从开始位置开始查找，一次匹配
        -search:从任何位置查找，一次匹配   案例22
        -findall:全部匹配，返回列表        案例23
        -finditer：全部匹配，返回迭代器    案例23
        -split：分割字符串，返回列表
        -sub：替换
    -匹配中文
        -中文unicode范围主要在[u4e00-u9fa5]
        案例v24
    -贪婪与非贪婪模式
         贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
         非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配
         -python里面数量词默认的是贪婪模式
         例如
              查找全文 abbbbbbccc
                re=ab*
                贪婪模式：结果是abbbbbb
                非贪婪：结果是a   
                
#XML
        -http://www.w3school.com.cn/xml/index.asp      
        -案例 v25
        -概念：父节点，子节点，先辈节点，兄弟节点，
#xpath
      -是一门在xml文档中查找信息的语言
      官方文档：http://www.w3school.com.cn/xpath/index.asp
      常用路径表达式：nodename:选取此节点的所有子节点
                     / :从根节点开始
                     // :选取元素，而不考虑元素的具体位置
                     .  :当前节点
                     .. :父亲节点
                     @  ：选取属性


# lxml库 
       python的HTML/XML的解析器
       官方文档：http://lxml.de/index.html      
       功能：
            -解析HTML  :  案例v26              
            -文件读取 ：案例v27.html   案例v28.py
            -etree和xpath配合使用   案例v29
        
        
#BeautifulSoup4
           官方文档 
                 http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/ 
           几个常用提取信息的工具比较
             1.正则 ：很快，不好用，不需安装
             2.beautifulsoup：慢，使用简单，安装简单
             3.lxml:比较快，使用简单，安装一般   
           案例v30
     -四大对象
           1.Tag
                -对应html中的标签
                -可以通过soup.tag_name(标签名称)
                -tag两个重要属性
                   -name
                   -attrs
                案例v31
           2.NavigableString
                 对应内容值   .string
                 案例v31
           
           3.BeautifulSoup
                -表示的是一个文档的内容，大部分把他当做是tag对象
                -一般我们可以用soup表示
           4.Comment 
              -特殊类型的NavigableString的对象
              -对其输出，则内容不包括注释符号
     -遍历一个文档对象
          -contents :tag的子节点以列表的方式给出
          -children：子节点以迭代器形式返回
          -descendants:所有子孙节点
          -string
          案例 v32
          
     搜索文档对象
        find_all()        
           
#CSS选择器
     -使用soup.select,返回一个列表
     -通过标签名称，soup,select("title")
     -通过类名：soup,select(".content")
     -id查找：soup.select("#name_id")
     -组合查找：soup.select("div #input_content")
     -属性查找：soup.select("img[class='photo']")
     -获取tag内容：tag.get_text
     -案例v33
     

                      
     