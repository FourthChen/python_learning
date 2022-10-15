def EX_GCD(a,b,arr): #扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g

def ModReverse(a,n): #ax=1(mod n) 求a模n的乘法逆x
    arr = [0,1,]
    gcd = EX_GCD(a,n,arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1


a=input("请输入乘数：")
b=input("请输入模数：")
a=50**58
b=97
arr = [0,1,]
print(a,'模',b,'的乘法逆：',ModReverse(a,b))
print(a,'和',b,'的最大公约数：',EX_GCD(a,b,arr))
print(arr[1],'×',b,'+',arr[0],'×',a,'= 1')
