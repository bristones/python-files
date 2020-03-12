        #a program to output a Customer name, Account Details and their Balances
from Customer_details import Customer
from Account import Account
from Currency import Currency

print("welcome to your account\n")
print("select the following options;\n")

#customer options:
1=checkBalance
2=SendMoney
3=Exit

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

print("************* "Account Balance", ****************")
 


print("************* "hahaha", ****************")