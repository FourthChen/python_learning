
#sys是和python解释器打交道的
import sys
# sys.argv
print(sys.argv) #argv的第一个参数， 是python这个命令后面的值
# sys.path
print( sys.path)

#一个模块能否被顺利导入  全看sys.path下面有没有这个模块所在
# sys.modules
print(sys.modules)#是我们导入到内存中的所有模块的名字：这个模块的命名空间 