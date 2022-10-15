#闭包，在内层函数中访问外层函数的变量
#闭包的作用：
    # 1.可以保护你的变量不受侵害
    # 2.可以让一个变量常驻内存
# def outer():
#     a=10   #对外界是不开放的
#     def inner():
#         print(a)
#     return inner
# fn=outer()
# fn()

#超简单爬虫
# from urllib.request import urlopen
# def outer():
#     #常驻内存
#     s=urlopen('').read()
#     def getcontent():   #闭包
#         return s
#     return  getcontent
#
# pa=outer()
# print(pa())