
import re
#永远不要起一个py文件的名字  这个名字和你已知的模块同名

# 查找
# findall：匹配所有，每一项都是列表中的一个元素
# ret=re.findall('\d+','adakjdke23但是看见sdkj899')
# print(ret)
# search：只匹配从左到右的第一个，得到的是变量，通过这个变量的group()方法来获取结果
# ret=re.search('\d+','adakjdke23但是看见sdkj899')
# print(ret)  #内存地址，这是一个正则匹配的结果
# print(ret.group()) #通过ret.group()获取真正的结果
# ret=re.search('\d+','adakjdke23但是看见sdkj899')
# if ret:
#     print(ret.group())
# match:从头开始匹配，相当于search中的正则表达式加一个^

#字符串处理的扩展：替换切割
#split
# s='alex83taibai40egon25'
# ret=re.split('\d+',s)
# print(ret)
#sub
# ret=re.sub('\d+','H','alex83taibai40egon25')
# print(ret)
# #subn  返回一个元组，第二个元素是替换的次数
# ret=re.subn('\d+','H','alex83taibai40egon25')
# print(ret)

#re模块的进阶
#compile   节省你使用正则表达式解决问题的时间
  #编译  正则表达式 编译成字节码
  #在多次使用过程中 不会多次编译
# ret=re.compile('\d+')  #已经完成了编译
# print(ret)
# res=ret.findall('sdsjkks232dsssd')
# print(res)
#finditer  节省你使用正则表达式解决问题的空间
ret=re.finditer('\d+','dshjdhsj232482ddsd98')
print(ret)
for i in ret:
    print(i.group( ))