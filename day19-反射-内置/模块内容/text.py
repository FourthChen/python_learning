
import master

while 1:
    print("""
    大牛写了很多个功能
    chi
    he
    la
    
    """)
    val=input('请输入你想要测试的功能：')
    if hasattr(master,val):
        func = getattr(master, val)  # 从xxx对象或者模块中找xxx功能（字符串）
        if callable(func):#判断这个是否可以被调用
            func()
        else:
            print(func)    
    else:
        print("没有这个功能")
    # if val=='chi':
    #     master.chi()
    # if val=='he':
    #     master.he()
    # if val=='la':
    #     master.la()