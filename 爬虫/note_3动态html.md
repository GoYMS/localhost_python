#动态html
               -JavaScript
               -jQuery
               -ajax       
               -DHTML
       -Python采集动态数据
           -从JavaScript代码入手采集
           -Python第三方库进行JavaScript，直接采集你在浏览器看到的页面
           
# selenium +PhantomJS
    -Selenium: web自动化测试工具
        -自动加载页面
        -获取数据
        -截屏
        -安装 ：cmd  -》 pip install selenium==2.48.0
        -官网：http://selenium-python.readthedocs.io/index.html
    PhantomJS(幽灵浏览器) 
        -基于Webkit的无界面的浏览器
        -官网：https://phantomjs.org/download.html
    
    Selenium 库有一个WebDriver的API，WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
    案例v34
    
    - chrome +chromedriver
      - 下载安装chrome 
      - 下载安装chromedriver
      
    - Selenium操作主要分两大类
       - 得到UI元素
           - find_element_by_id
           -find_element_by_name
           -find_element_by_xpath
           -find_element_by_link_text
           -find_element_by_partial_link_text
           -find_element_by_tag_name
           -find_element_by_class_name
           -find_element_by_css_selector
          
       -基于UI元素操作的模拟
           单击，右键，拖拽，输入 都可以通过导入ActionsChains类来做到
       
       案例v35
       
       