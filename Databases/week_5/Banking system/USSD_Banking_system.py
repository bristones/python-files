        #a program to output a Customer name, Account Details and their Balances
import mysql.connector
from Customer_details import Customer
from account import Account
from Currency import Currency
from Functions import customerDetailsInDb
from Functions import accountInDb
#from Functions import 


mydbConnection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="12345678",
    database="school"
)


print("welcome to your account\n")
print("select the following options;\n")
print("1-check Balance\n","2-Send Money\n","3-Exit\n")


#check balance option
option = int(input("choose\n1-check Balance\n2-Send Money\n3 -Exit\n")
              
if option == 1:
    customerId=input("enter customerId")
    accNo=int(input("enter account number?"))
    customerDetailsInDb
    accountInDb
    print()
    #sending money option 
elif option ==2:
    customerId=input("enter your customerId")
    amount=int(input("amount to send"))
    name=input("Name of person")
    mobNo=input("Mobile number")
    print("Confirmed! You've send Ksh {} to {} of {}".formart(amount,name,mobNo))
#exit option
elif option==3:
    print("exit")
else:
    print("invalid number")


