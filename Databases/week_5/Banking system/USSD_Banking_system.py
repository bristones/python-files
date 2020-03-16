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
    passwd="@5*Star123456",
    database="school"
)


print("welcome to your account\n")
print("select the following options;\n")

#customer options:
select_1='checkBalance'
select_2='SendMoney'
Select_3='Exit'


#check balance option
if select_1:
    firstName=input("enter first name")
    accNo=int(input("enter account number?"))
    customerDetailsInDb
    accountInDb
    print()
    #sending money option 
elif select_2:
    amount=int(input("amount to send"))
    name=input("Name of person")
    mobileNo=input("Mobile number")
    print("Confirmed! You've send Ksh {} to {} of {}".formart(amount,name,accNo))
#exit option
elif Select_3:
    print("exit")
else:
    print("invalid number")


