import shelve

#打开一个文件
f=shelve.open("大阳哥",writeback=True)
#像操作字典一样操作文件
# f['gay']="周杰伦"
# print(f['jay'])

# f['jay']={"name":"周杰伦","age":10}
# f['jay']['name']='胡辣汤'
# print(f['jay']['name'])
# f.close()
