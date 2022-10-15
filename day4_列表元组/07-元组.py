
# print((1+3)*5)

# tu=(3, )#元组中如果只有一个元素，需要在括号中写一个，
# tu=tuple()  #空元组
#
# print(type(tu))

# tu=('人民币','美元','欧元')
# # tu.append('hhh')      #元组不能加
# # print(tu)
#
#
# print(tu[2])  #可以切片

#元组的第一层是不能赋值的，内部元素是没有要求的
tu=(1,'halou','how are you ',[])
tu[3].append('123')
print(tu)