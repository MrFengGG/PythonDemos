from configparser import ConfigParser

CONFIGFILE = 'f:\\python.txt'

config = ConfigParser()
#读取配置文件
config.read(CONFIGFILE)

#打印出事的问候有:
#要查看的区段是'message'
print(config.get('messages','greeting'))

#使用配置文件的一个问题读取半径:
radius = input(config.get('messages','question'))

#打印配置文件中的结果信息
#以逗号结束,在同一行显示:
print(config.get('messages','result_message'))

print(config.getfloat('numbers','pi') * float(radius)**2)
