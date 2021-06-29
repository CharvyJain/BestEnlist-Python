
import mysql.connector as msq

conn = msq.connect(host='localhost', user='root', password='password')
curs = conn.cursor(buffered=True)

curs.execute('SELECT VERSION()')
vers = curs.fetchone()
print('MySql Version:', vers)
