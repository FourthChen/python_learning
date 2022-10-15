# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 18:51
# @Author  : sihao
# @File    : 17-栈的应用-括号匹配问题.py
'''
给定一个字符串，其中包含小括号，中括号，大括号，
求该字符串中的括号是否匹配
'''
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def brance_match(s):
    match={'}':'{',']':'[',')':'('}
    stack=Stack()
    for ch in s:
        if ch in {'(','{','['}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.peek()==match[ch]:
                stack.pop()
            else: #stack.peek()!=match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False

print(brance_match('{{()[()]}}'))
print(brance_match('()(){}{}{}[{([)}]'))

