#encoding=utf-8
import pymysql
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123',
    db='mybase',
    charset='utf8'
    )
curs = conn.cursor()
sql = 'select * from moves where movename like \'%钢铁侠%\''
print(sql)
curs.execute(sql)
moves = curs.fetchall()
for move in moves:
    print(move)
