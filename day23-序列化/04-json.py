# wf={
#     "name":"汪峰",
#     "age":10,
#     "hobby":"抢头条",
#     "wife":{
#         "name":"子怡",
#         "age":30
#     }
# }
import json
# dic={"a":"理查德姑妈","b":"雄霸","c":"天下"}
#如果你的key或者value超出了ASCII范畴，就会显示\uxxx
# s=json.dumps(dic,ensure_ascii=False)
# print(repr(s),type(s))
#
# #把json解析成字典
# dic1=json.loads(s)
# print(dic1,type(dic1))

# f=open("wa.json",mode="w",encoding="utf-8")
# json.dump(dic,f,ensure_ascii=False)#把json写入文件中去
# f.close()

# #读出
# f=open("wa.json",mode="r",encoding="utf-8")
# s=json.load(f) #把文件中的json字符串读出成字典
# print(s,type(s))

# lst=[{"a":1},{"b":2},{"c":3},{"d":4},{"e":5}]
# f=open("menu.json",mode="w",encoding="utf-8")
# for dic in lst:
#     json.dump(dic,f,ensure_ascii=False)
#
# f.close()
#
# f=open("menu.json",mode="r",encoding="utf-8")
# s=json.load(f)
# print(s,type(s))
f=open("menu.json",mode="w",encoding="utf-8")
lst=[{"a":1},{"b":2},{"c":3},{"d":4},{"e":5}]
for el in lst:
    s=json.dumps(el, f, ensure_ascii=False)+"\n"
    f.write(s)

f.flush()
f.close()

f=open("menu.json",mode="r",encoding="utf-8")
for line in f:
    line=line.strip()  #去掉换行
    dic=json.loads(line)
    print(dic)