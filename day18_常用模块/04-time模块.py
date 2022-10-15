
import time
# time.sleep(2)  #程序走到这里回等待2s
#time模块主要是用来和时间打交道
#时间格式
    # '2019-09-01'  '2019.8.20' 字符串数据类型  格式化时间 给人看的
    # 1567773477.9515417  浮点型数据类型   以s为单位  时间戳时间  给机器计算用的
# print(time.time())

#格式化时间
# print(time.strftime('%Y-%m-%d %H-%M-%S')) #str format time
# print(time.strftime('%c'))

#结构化时间
# print(time.localtime()) #北京时间

#时间戳换成字符串时间
print(time.time())#1567931378.9667556
struct_time=time.localtime(1567931378.9667556)
ret=time.strftime('%y/%m/%d %H:%M:%S',struct_time)
print(ret)

#字符串时间 转时间戳
struct_time=time.strptime('2018-9-8','%Y-%m-%d')
print(struct_time)
res=time.mktime(struct_time)
print(res)
