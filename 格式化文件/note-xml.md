#结构化文件存储
    -为了解决不同设备之间信息交换
#xml文件
    参考资料
     1.https://docs.python.org/3/library/xml.etree.elementtree.html
     2.http://www.runoob.com/python/python-xml.html
     3.https://blog.csdn.net/seetheworld518/article/details/49535285
#XML 指可扩展标记语言（eXtensible Markup Language）
     -标记语言：语言中使用尖括号括起来的文本字符串标记
     -可扩展：用户可以自己定义需要的标记
     -xml描述的是数据本身，即数据的结构和语义
#xml文档的构成
      -处理指令（可以认为一个文件内只有一个处理指令）
      -根元素（一个文件内只有一个根元素）
      -子元素
      -属性
      -内容
      -注释    
      
#xml标签的命名规则
      -Pascal命名法
      -用单词表示，第一个字母大写
      -大小写严格区分
      -配对的标签必须一致
#命名空间
      -为了防止命名冲突
      -为了避免冲突，徐亚奥给可能冲突的元素加命名空间   xmlns
#xml访问
     -读取
     -xml读取分两个主要技术：SAX,DOM
     -SAX：
          -基于事件驱动API
          -利用1SAX解析文档设计到解析器和事件处理两部分
          -特点：1.快  2.流式读取
     -DOM ；
          -是W3C规定的xml编程接口
          -一个xml文件在缓存中以树形结构缓存，读取
          -用途
               -定位浏览xml任何一个节点信息
               -添加删除相应内容
          -相应方法的包
             -minidom
                 -minidom.parse(filename):加载读取的xml文件，filename也可以是xml代码
                 -doc.documentElement:获取xml文档对象，一个xml文件只有一个对于的文档对象
                 -node.getAttribute(attr_name):获取xml节点的属性值
                 -node.getElementByTagName(tage_name):得到一个节点对象集合
                 -node.childNodes;得到所有孩子节点
                 -node.childNodes[index].nodeValue:获取单个节点值
                 -node.firstNode;得到第一个节点，等价于node.childNodes[0]
                 -node.attributes[tage_name]
             -etree
                 -以树形结构来表示xml
                 -root.getiterator:得到相应的可迭代的mode集合
                 -root.iter
                 -find(node_name):查找指定node_name的节点，返回一个node
                 -root.findall(node_name):返回多个node_name的节点
                 -node.tag；node对应的tagename
                 -node.text;node的文本值
                 -node.attrib:是node的属性的字典类型的内容
#xml文件写入
     -更改
         -ele.set:修改属性
         -ele.appendd;添加子元素
         -ele.remove:删除元素
     -生产创建
         -SubElement
         -minidom写入
         -etree写入
         
            
         
            

      
    