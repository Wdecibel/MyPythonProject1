# __Author__: Han
# __Date__: 2019/1/18

# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xml_test")
# root = tree.getroot()
# print(root.tag)

# # 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text)
#
# # 只遍历year 节点
# for node in root.iter('year'):
#     print(node.tag, node.text)


import xml.etree.ElementTree as ET

tree = ET.parse("xml_test")
root = tree.getroot()
#
# # 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated", "yes")
#
# tree.write("xmltest.xml")

# # 删除node
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')


import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
age.text = '33'
sex = ET.SubElement(name, "sex")
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式



