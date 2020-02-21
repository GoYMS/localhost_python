from lxml import etree

#只能读取xml格式内容
xml = etree.parse("./v27.xml")

#xpath的意思是查找带有category属性值为sport的book元素
rst = xml.xpath('//book[@category="sport"]')
print(rst)

#xpath的意思是查找带有category属性值为sport的book元素下边year元素
rst = xml.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(rst.tag)
print(rst.text)