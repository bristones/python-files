import mysql.connector


#Establish the DB connection
def Connection():
    mydbConnection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="12345678",
    database="school"
    )
    return mydbConnection

#customer details function
def customerDetailsInDb(customer_Details):
    myDbConnection = Connection()
     mycursor=myDbConnection.cursor()
    mycursor.execute("SELECT firstName, lastName FROM customers") 
    print(mycursor.execute, "Your account details are;")
    


#account function
def accountInDb(account):
    myDbConnection = Connection()
    mycursor=myDbConnection.cursor()
    mycursor.execute("SELECT accType, accBal FROM account")
    print(mycursor.execute, "Your account balance is:")


#account function
#def subjectIntoDatabase(subject):
#    myDbConnection = Connection()
#   my_sql = "insert into subjects(subjectName, subjectScore)Values(%s,%s)"
#    val = (subject.subjectName, subject.subjectScore)
#    mycursor=myDbConnection.cursor()
#    mycursor.execute(my_sql, val)
#    myDbConnection.commit()
#    print(mycursor.rowcount, "entry recorded to subjects Table")

    