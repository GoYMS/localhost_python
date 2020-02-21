from lxml.html import etree
"""
用lxml来解析html代码
"""

text ='''
<div>
   <ul>
     <li class="item_1"><a href="0.html">item</a><li>
     <li class="item_2"><a href="0.html">item</a><li>
     <li class="item_3"><a href="0.html">item</a><li>
   </ul>
</div>

'''

#利用etree，html把字符串解析成HTML文档

html = etree.HTML(text)
s = etree.tostring(html)
print(s)
