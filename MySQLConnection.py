import mysql.connector

myDB = mysql.connector.connect(host="localhost", user="Shubham", passwd="220898", database="Test")

myCur = myDB.cursor()

myCur.execute("select * from student")

for i in myCur:
    print(i)