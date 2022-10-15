# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 17:38
# @Author  : sihao
# @File    : hashlib模块.py

import hashlib

# md5=hashlib.md5()
# md5.update(b"hello")
#
# print(md5.hexdigest())
# print(len(md5.hexdigest()))
#

md5=hashlib.md5()
with open("ssh_client.py",'rb') as f:
    md5.update(f)

print(md5.dexdigest())