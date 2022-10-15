
#递归函数
# count=1
# def func():
#     global count
#     print('123',count)
#     count=count+1
#     func()
# func()
# #递归深度，你可以自己调用自己的次数，官网文档最大深度是1000
#遍历E:/文件夹，打印出所有的文件和普通文件的文件名

import os
def func(filename,n):
    #1.打开这个文件夹
    files=os.listdir(filename)  #查看当前目录中的文件
    #2.拿到这个文件夹
    for file in files:  #获取每一个文件
        #3.获取到文件的路径
        file_p=os.path.join(filename,file)
        #4.判断是否是文件夹
        if os.path.isdir(file_p):  #判断file_p是否是一个文件夹
            print("\t"*n,file,":")
            func(file_p,n+1)
        else: #不是文件夹，普通文件
            print("\t"*n,file)
func("E:/python学习",0)