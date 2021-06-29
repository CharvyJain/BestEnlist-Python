curs.execute('CREATE DATABASE mydb')

conn = mysql.connector.connect(host='localhost', user='root', password='password', database='mydb')
curs = conn.cursor(buffered=True)

curs.execute('CREATE TABLE student(Stu_Id INTEGER(7), Stu_Name VARCHAR(255), Stu_Dept VARCHAR(255))')
curs.execute('CREATE TABLE staff(Staff_Id INTEGER(7), Staff_Name VARCHAR(255), Staff_Dept VARCHAR(255))')

curs.execute("SHOW TABLES")
for value in curs:
    print(value)
# ('staff',)
# ('student',)

query = 'INSERT INTO student(Stu_Id, Stu_Name, Stu_Dept) VALUES(%s, %s, %s)'
data = [(234, 'John', 'CSE'), (535, 'Chris', 'ECE'), (782, 'Sara', 'CSE')]
for value in data:
    curs.execute(query, value)

query = 'INSERT INTO staff(Staff_Id, Staff_Name, Staff_Dept) VALUES(%s, %s, %s)'
data = [(922, 'David', 'CSE'), (452, 'Rose', 'ECE')]
for value in data:
    curs.execute(query, value)

# Displaying Student details
curs.execute('SELECT * from student')
student = curs.fetchall()
for details in student:
    print(details)
    
# Students
# (234, 'John', 'CSE')
#(535, 'Chris', 'ECE')
#(782, 'Sara', 'CSE')
