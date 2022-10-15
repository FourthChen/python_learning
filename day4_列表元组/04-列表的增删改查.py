
# lst=['赵四','施瓦辛格','黄渤','郭达神']
# #在屁股后面添加
# lst.append('黄宏')  #在原有的基础上进行的操作
# #在××位置插入xx内容
# lst.insert(1,'王力宏')
# lst.extend(['马化腾','马云']) #迭代添加
#
# print(lst)

#删除
# data=lst.pop(2)  #返回被删除的数据
# print(data)
# print(lst)

# lst.remove('赵四')  #删除元素
# print(lst)

#切片删
# del lst[1:3]
# print(lst)

#清空
# lst.clear()
# print(lst)

#改
lst=['王者荣耀','魔兽世界','dnf','cs']
# lst[0]='扫雷'
# print(lst)
# lst[1:3]=['跑跑卡丁车']  #先删除后添加
# lst[1::2]=['qq三国','qq华夏']   #切片修改的时候，如果步长不是1，注意数量
# print(lst)

#查询
for i in lst:
    print(i)