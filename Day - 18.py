//1. Create a DB with doctor and doctor ID & patients visited

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="123456",
  database = "Dc"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Doctors (dr_name VARCHAR(255),dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
dbse = mydb.cursor()
sql = "INSERT INTO Doctors (dr_name,dr_id , Patients_visited) VALUES (%s,%s,%s)"
val = [('CHARVY','56',10),('AHANA','59',5),('Rachel','25',0)]
dbse.executemany(sql, val)
mydb.commit()
print(dbse.rowcount, "was inserted.")

//2. Get the doctor(s) who have more than 5 patients visited
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")
myresult = mycursor.fetchall()
for y in myresult:
  print(y)

//3. Get the doctors with no patients visit
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_visited =0")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
