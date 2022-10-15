from 数据结构的学习 import Stack
''''
把十进制转化为二进制
'''

def div_by2(def_number):
    restack=Stack.stack()

    while def_number >0:
        rem=def_number %2
        restack.push(rem)
        def_number=def_number//2

    bin_string=""
    while not restack.is_empty():
        bin_string=bin_string+str(restack.pop())
    return bin_string
print(div_by2(42))
'''
转化为n进制
其中base为多少进制
'''
def div_byn(def_number,base):
    digits="0123456789ABCDEF"
    restack=Stack.stack()

    while def_number >0:
        rem=def_number %base
        restack.push(rem)
        def_number=def_number//base

    bin_string=""
    while not restack.is_empty():
        bin_string=bin_string+digits[restack.pop()]
    return bin_string
print(div_byn(42,16))