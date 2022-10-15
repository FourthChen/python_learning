#先进后出
#抽象数据类型“栈”是一个有次序的数据集
'''
stack(): 创建空栈
push（item）: 将item加入栈顶，无返回值
pop(): 将返回栈顶数据项移除，并返回，栈被修改
peek(): "窥视"栈顶数据项，返回栈顶的数据项但不移除，栈不被修改
isEmpty(): 返回栈是否为空栈
size(): 返回栈中有多少个数据项
'''
class stack:
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


a=stack()
a.push(1)
a.push(2)
a.push(3)
print(a.pop())
print(a)