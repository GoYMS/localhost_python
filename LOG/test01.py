"""
import logging

#定义好的可以用于format格式字符串中字段
LOG_FORMAT="%(asctime)s====%(levelname)====%(message)s"

#该方法用于为logging日志系统做一些基本配置
logging.basicConfig(filename="rizhixinxi.txt",level=logging.DEBUG,format=LOG_FORMAT)

#打印各种日志的方法
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
#另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
"""

"""
#习题练习
import logging

#打印出来的格式
LOG_FORMAT="%(asctime)s====%(levelname)s====%(message)s"
#默认情况下为什么只打印出来后三个？？
#原因：因为下边的basicConfig默认的level是从waring开始，所以默认情况下是只打印出来waring后边高等级的
logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT,filename="rizhixinxi.txt")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
"""

#装饰器
#使用装饰器，打印函数执行时间

