
#range（）是一个可迭代对象
#1.range(1,n)   从1到n-1
# for i in range(10):
#     print(i)
# #2.range(m,n)   从m到n-1
# for i in range(1,4):
#     print(i)
#
# #3.range(m,n,q)  从m到n每q个取一个
# for i in range(1,10,2):
#     print(i)

#获取到列表的索引，拿到索引之后，可以拿到元素
lst=['砂锅','馒头','盖浇饭','刀削面']
for i in range(len(lst)):
    print(i)   #i 是lst的索引
    print(lst[i])