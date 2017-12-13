import sys,shelve
def store_person(db):
    """
    用于存储数据的函数
    """
    pid = input('请输入唯一的编号')
    person = {}
    person['名字'] = input('请输入姓名')
    person['年龄'] = input('请输入年龄')
    person['电话'] = input('请输入电话号码')
    db[pid] = person
def look_up(db):
    """
    根据id查询人
    """
    pid = input('输入id')
    field = input('你想知道什么信息?(名字,年龄,电话号码)')
    field = field.strip().lower()   #去掉空格,将字符变为小写
    print (field+':'+ db[pid][field])   #首字母大写
def print_help():
    print('store:储存个人信息')
    print('lookup:以id查询个人信息')
    print('quit:退出')
    print('?:查看帮助')
def enter_command():
    cmd = input('输入一个命令(?获取帮助)')
    cmd = cmd.strip().lower()
    return cmd
def main():
    database = shelve.open('f:\\database.dat')
    try:
        while True:
            cmd = enter_command()
            if(cmd == 'store'):
                store_person(database)
            elif(cmd == 'lookup'):
                look_up(database)
            elif(cmd == 'quit'):
                return;
            elif(cmd == '?'):
                print_help()
    finally:
        database.close()
if __name__ == '__main__':
    main()
            
                    
        
    
