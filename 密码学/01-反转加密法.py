#反转加密法
#reverse cipher



message=str(input("请输入需要反转加密的消息："))

translated=''

i=len(message)-1
while i>=0:
    translated=translated+message[i]
    i=i-1
print("反转后的消息为：",translated)