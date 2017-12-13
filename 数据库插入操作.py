import sqlite3
conn = sqlite3.connect('person.db')
curs = conn.cursor()


query = 'INSERT INTO person (name,age) VALUES(?,?)'
name = input('请输入姓名')
age = input('请输入年龄')
curs.execute(query,[name,age])
conn.commit()
conn.close()
			
