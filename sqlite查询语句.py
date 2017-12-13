import sqlite3
conn = sqlite3.connect('person.db')
curs = conn.cursor()

sql = 'SELECT * FROM person'
curs.execute(sql)
persons = curs.fetchall()
for person in persons:
    print(person)
