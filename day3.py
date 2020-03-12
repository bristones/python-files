import mysql.connector
mydbConnection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="@5*Star123456",
    database="my_schools_db"
    )

Cursor = mydbConnection.cursor()
Cursor.execute("SELECT * FROM mashule")
mashule = Cursor.fetchall()
for sch in mashule:
    print(sch)

Cursor = mydbConnection.cursor()
Cursor.execute("UPDATE mashule set name = [mercy]* WHERE name")
for mash in mashule:
    print(mash)

