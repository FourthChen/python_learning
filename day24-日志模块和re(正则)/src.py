# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 16:45
# @Author  : sihao
# @File    : src.py


#拿到日志的产生者即loggers，
#第一个日志的产生者

#需要先导入日志配置LOGGING_DIC
import setting
from logging import config,getLogger

config.dictConfig(setting.LOGGING_DIC)
logger1=getLogger('测试')

logger1.info('这是一条info')

#补充两个重要的知识点
#1.日志轮转
#    日志记录着程序员运行过程中的关键信息
#2.日志的命名
#    日志命名时区别日志业务归属的一种非常重要的标识

