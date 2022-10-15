# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 09:48
# @Author  : sihao
# @File    : 19-栈的的应用-迷宫问题.py
'''
栈---深度优先搜索
    回溯法-----使用栈储存当前路径

'''
#1表示围墙，0表示空地
maze=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dirs=[
    lambda x,y:(x-1,y),
    lambda x,y:(x+1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1)
]
def maze_path(x1,y1,x2,y2):
    stack=[]
    stack.append((x1,y1))
    while(len(stack)>0):
        curNode=stack[-1] #当前的节点
        if curNode[0]==x2 and curNode[1]==y2:
            #走到终点
            for p in stack:
                print(p)
            return  True
        for dir in dirs:
            nextNode=dir(curNode[0],curNode[1])
            #如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]]==0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 #标记为已经走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False

maze_path(1,1,8,3)