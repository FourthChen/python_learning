
# s='alex'
# print(s.encode('utf-8'))    #b'alex'
# #encode() 为编码
#
# #bytes

s='饿了么'
s1=s.encode('utf-8')
print(s.encode('utf-8'))  #编码  结果为：  b'\xe9\xa5\xbf\xe4\xba\x86\xe4\xb9\x88'
print(s1.decode('gbk'))   #解码  结果为：  饿了么