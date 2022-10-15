from xml.etree import ElementTree as ET
'''
XML格式的数据既便于机器读取，也便于人工读取
find返回的是匹配到的第一个元素，而findall返回的是匹配的所有元素
attrib可以返回每一个节点的属性
'''
tree=ET.parse('E:/python学习/数据分析/数据/data-text.xml')
root=tree.getroot()

data=root.find('Data')

all_data=[]
for observation in data:
    record ={}
    for item in observation:
        lookup_key=list(item.attrib.keys())[0]
        if lookup_key =='Numeric':
            rec_key='NUMERIC'
            rec_value=item.attrib['Numeric']
        else:
            rec_key=item.attrib[lookup_key]
            rec_value=item.attrib['Code']

        record[rec_key]=rec_value
    all_data.append(record)
print(all_data)