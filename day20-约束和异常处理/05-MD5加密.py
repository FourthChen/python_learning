
import hashlib
# #1.
# obj=hashlib.md5(b"kjakjfhalkjflakjspovjslkfs")#加盐
#
# #把你要加密的内容给md5
# obj.update("123".encode("utf-8"))#必须时字节
#
# #3.获取密文
# val=obj.hexdigest()
# print(val)

def md5(val):
    obj=hashlib.md5(b"dad")
    obj.update(val.encode("utf-8"))
    val=obj.hexdigest()
    return val

#注册的时候，用md5进行加密，存储的是 加密后的密文
username=input("请输入用户名：")
password=input("请输入密码：")
if username=="alex" and md5(password)=="7fd4213dc713984d1751ef7f27ed9767":
    print("登录成功")
else:
    print("登录失败")

