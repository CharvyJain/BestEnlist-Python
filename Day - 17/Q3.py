# Creating table, 'Employee' and inserting value in it
curs.execute('CREATE TABLE Employee(EmpId INTEGER(7), EmpName VARCHAR(255), EmpSal INTEGER(7))')
sql = 'INSERT INTO Employee(EmpId, EmpName, EmpSal) VALUES(%s, %s, %s)'
data = [(45687, 'Jhanvi', 20000), (15689, 'Chinni', 28000), (7682, 'Sirisha', 60000)]
for value in data:
    curs.execute(sql, value)

curs.execute('SELECT EmpName from Employee')
employee = curs.fetchall()

for name in employee:
    print(name[0])
    
# Employees
# Jhanvi
# Chinni
# Sirisha

curs.execute('DROP DATABASE mydb')

conn.commit()
curs.close()
conn.close()
