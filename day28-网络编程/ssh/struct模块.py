# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 16:54
# @Author  : sihao
# @File    : struct模块.py

import struct
res=struct.pack("i",11232333)

print(res)
print(len(res))

obj=struct.unpack("i",res)
print(obj)