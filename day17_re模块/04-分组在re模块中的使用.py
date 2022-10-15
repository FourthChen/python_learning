import re
s='<a>fdd</a>' #标签语言
# ret=re.search('<(\w+)>(\w+)</(\w+)>',s)
# print(ret.group())#所有的结果
# print(ret.group(1))#数字参数代表的是取对应分组中的内容
# print(ret.group(2))
# print(ret.group(3))

#findall 也可以顺利取到分组中的内容，有一个特殊的语法就是优先显示分组中的内容
ret=re.findall(">(\w+)<",s)
print(ret)