import logging

logging.basicConfig(filename='xl.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=0)#  level 设置级别，但你的信息的级别>=level的时候才会写入日志文件

#写日志
logging.critical("我是critical")  #50
logging.error("我是error") #40
logging.warning("我是警告")  #30
logging.info("我是基本信息")  #20
logging.debug("我是调试") #10
logging.log(2,"我是自定义")

#多文件日志处理