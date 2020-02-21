from lxml import etree
#parse只能读取xml格式内容，html不能读取
html = etree.parse("./v27.xml")

rsp = etree.tostring(html,pretty_print=True)
print(rsp)
