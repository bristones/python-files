        #a program to output a Customer name, Account Details and their Balances
bankCustomers=dict()
customer=dict()
account=dict ()
currency=dict()
            
firstName=input("the customer's first name")
lastName=input("the customer's last name")
mobNo=input("the customer's mobNo")
idNo=input("the customer's Id number")
customerId=input("the customer ID")

customer['firstName']=firstName
customer['lastName']=lastName
customer['mobNo']=mobNo
customer['id']=idNo
customer['Id']=customerId


bankCustomers[customerId]=customer
            
AccNo=input("enter the customer AccNo")
AccType=input("enter the customer Account type")
AccCurrency=input("enter the customer Account currency")
AccBal=int(input("enter the customer Account Balance"))
account['No']=AccNo
account['Type']=AccType
account['Currency']=AccCurrency
account['Bal']=AccBal

customer['AccountNumber']=account

currencyCode=int(input("enter the currency code"))
currencyName=(input("enter the currency name"))
currency['code']=currencyCode
currency['name']=currencyName

account[currencyCode]=currency

print("*"*15, "ACCOUNT BALANCE","*"*15)
for k,v in bankCustomers.items():
    print([firstName], [lastName])
    print("Account No:",[AccNo])
    print("balance:",[AccBal]) 


print("*"*15, "hahaha","*"*15)