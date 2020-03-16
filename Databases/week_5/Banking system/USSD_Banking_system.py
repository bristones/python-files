        #a program to output a Customer name, Account Details and their Balances
import mysql.connector
from Customer_details import Customer
from Account import Account
from Currency import Currency
from Functions import customerDetailsInDb
from Functions import studentIntoDatabase
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
    accountInDd
    print()
    elif select_2: 



    
    


#send money option



#exit option





if 1:
    print("This is your balance")
    if 2:
        amount=int(input("amount to send"))
        name=input("Name of person")
        mobileNo=input("Mobile number")
        print("send Ksh{} to {} of {}".formart(amount,name,MobileNo))
        if 3:
            print("exit")
        else:
                print("invalid number")


person_Details=[]

firstName=input("the customer's first name")
lastName=input("the customer's last name")
mobNo=input("the customer's mobNo")
idNo=input("the customer's Id number")
customerId=input("the customer ID")
#creating an instance
details=Customer(firstName,lastName,mobNo,idNo,customerId)
person_Details.append(details)

account_details=[]
AccNo=input("enter the customer AccNo")
AccType=input("enter the customer Account type")
AccCurrency=input("enter the customer Account currency")
AccBal=int(input("enter the customer Account Balance"))
#creating an instance
adetails=Account(AccNo,AccType,AccCurrency,AccBal)
account_details.append(adetails)

            



customer['AccountNumber']=account

currencyCode=int(input("enter the currency code"))
currencyName=(input("enter the currency name"))


account[currencyCode]=currency

print("************* Account_Balance ****************")
 


print("************* hahaha ****************")