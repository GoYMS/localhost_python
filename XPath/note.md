#XPath
      -在xml文件中查找信息的一套规则/语言，根据xml的元素或者属性进行遍历
      -http://www.w3school.com.cn/xpath/index.asp
#XPath 开发工具
     -开源的XPath表达式编辑工具：xmlQuire
     -Chrome插件：XPath Helper
     -Firefox插件：XPath Checker
#选取节点
     -nodename：选取次节点的所有子节点
     - /  :从根节点开始选取
     - //  :选取节点，不考虑位置
     - . :选取当前节点
     - .. :选取当前节点的父节点
     - @ :选取属性 
#XPath中查找一般按照路径的方法查找，以下是按照路径的方法进行查找
      
      
      School/Teacher :返回Teacher节点
      School/Student:返回两个Student节点
      //Student:选取所有Student的节点，不考虑位置
      School//Age :选取School后代中所有Age节点
      //@other ：选取other属性
      //Age[@Detail] :选取带有属性Detail的Age元素
      
#谓语 - Predicates
     /School/Student[1]:选取School下面的第一个Student节点
     /School/Student[last()]：选取School下面的最后一个Student节点
     /School/Student[last()-1]:选取School 下面倒数第二个Student节点
     /School/Student[position()<3]:选取School下面的前二个Student节点
     //Student[@score]:选取带有属性score的Student节点
     //Student[@score="99"]:选取带有属性score并且属性值是99的Student节点
     //Student[@score]/Age: 选取带有属性score的Student节点的子节点Age
     
     
#XPath 的一些操作
       |  :或者
        //Student[@score] | //Teacher  ;带有属性score的Student节点和Teacher节点
        
       其余不常见的XPath的运算符 + ,- , * ,div ,> ,<
      
           

     