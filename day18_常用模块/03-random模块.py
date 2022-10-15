#random模块---取随机数的模块
import random

# #取随机小数
# print(random.random())  #取0-1之间的小数
# print(random.uniform(1,2))  #取1-2之间的小数
# #取随机整数
# print(random.randint(1,2))#[1,2]
# print(random.randrange(1,2))  #[1,2) ,取不到2
# print(random.randrange(1,200,2)) #随机取奇数
# #从一个列表中随机取值：抽奖
# l=['a','b',(1,2),123]
# print(random.choice(l))
# print(random.sample(l,2)) #随机抽取两个
# #打乱一个列表的顺序，在原列表的基础上直接进行修改，节省空间
# #洗牌
# random.shuffle(l)
# print(l)


#验证码
    #四位数字验证码
    #六位数字验证码
    #六位数字字+母验证码
# s=''
# for i in range(4):
#     num=random.randint(0,9)
#     s+=str(num)
# print(s)
# def code(n):
#     s = ''
#     for i in range(n):
#         num = random.randint(0, 9)
#         s += str(num)
#     return s
# print(code(4))

#六位数字字+母验证码,一个位置上出现的是数字还是字母就是随机的
# print(chr(65))  用ascia码打印字母
# s=''
# for i in range(6):
#     #生成随机的字母，数字各一个
#     num=str(random.randint(0,9))
#     alpha_upper=chr(random.randint(65,90))
#     alpha_lower = chr(random.randint(97, 112))
#     # print(num,chr(alpha))
#     res=random.choice([num,alpha_lower,alpha_upper])
#     s+=res
# print(s)

def code(n):
    s = ''
    for i in range(n):
        # 生成随机的字母，数字各一个
        num = str(random.randint(0, 9))
        alpha_upper = chr(random.randint(65, 90))
        alpha_lower = chr(random.randint(97, 112))
        # print(num,chr(alpha))
        res = random.choice([num, alpha_lower, alpha_upper])
        s += res
    return s
print(code(6))

#发红包
    #红包数量 钱数
    #拼手气红包