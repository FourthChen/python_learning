# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 13:09
# @Author  : sihao
# @File    : 递归-可视化画树.py
import turtle
t=turtle.Turtle()
'''
正方形
'''
# for i in range(4):
#
#     t.forward(100)
#     #右转90度
#     t.right(90)
# turtle.done()

'''
红色五角星
'''
# t.pencolor('red')
# t.pensize(3)
# for i in range(5):
#     t.forward(100)
#     t.right(144)
#
# t.hideturtle()
#
# turtle.done()

'''
螺旋线
'''
# def drawSpiral(t,lineLen):
#     if lineLen>0:
#         t.forward(lineLen)
#         t.right(90)
#         drawSpiral(t,lineLen-2)
#
# drawSpiral(t,200)
# turtle.done()
'''
画树
'''
def tree(branch_len):
    if branch_len>5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15)
        t.left(40)
        tree(branch_len-15)
        t.right(20)
        t.backward(branch_len) #返回原位置

t=turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
t.hideturtle()
tree(100)
turtle.done()