

# for el in lst:
#     if el==n: #时间复杂度:O(n)
#         print("找到了")
#         break
#     else:
#         print('没有')
#         break

#使用二分法可以提高查找数据，前提条件：有序

# left=0
# right=len(lst)-1
# while left<right: #边界
#     mid=(left+right)//2   #必须整除，因为索引没有小数
#     if lst[mid]>n:
#         right=mid-1
#     if lst[mid]<n:
#         left=mid+1
#     if lst[mid]==n:
#         print('找到了')
#         break
# else:
#     print("没找到")
lst=[22, 33, 44, 55, 66, 77, 88, 99, 101, 433, 554, 3343, 3823, 5233]
# n=669
#递归完成二分法
def binary_searrch(n,left,right):

    if left <= right:
        mid = (left + right) // 2
        if lst[mid]>n:
            right=mid-1
            #深坑，函数的返回值返回给调用者
            return binary_searrch(n, left, right)
        elif lst[mid]<n:
            left=mid+1
            return binary_searrch(n, left, right)
        else:
            print('找到了')
            return mid
            #通过return返回，终止递归
    else:
        print('没有这个数')
        return -1
ret=binary_searrch(55,0,len(lst)-1)
print(ret)