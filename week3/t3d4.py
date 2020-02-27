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
    CustomerAcc=input("the customer account")
    customer['firstName']=firstName
    customer['lastName']=lastName
    customer['mobNo']=mobNo
    customer['id']=idNo
    customer['Id']=customerId
    customer['Acc']=customerAcc

    bankCustomers[customerId]=customer
    
        AccNo=input("enter the customer AccNo")
        AccType=input("enter the customer Account type")
        AccCurrency=input("enter the customer Account currency")
        AccBal=input("enter the customer Account Balance")
        account['No']=AccNo
        account['Type']=AccType
        account['Currency']=AccCurrency
        account['Bal']=AccBal

        customer[AccNo]=account

            currencyCode=int(input("enter the currency code"))
            currencyName=int(input("enter the currency name"))
            currency['code']=currencyCode
            currency['name']=currencyName

            account[currencyCode]=currency
    

for k,v in bankCustomers.items():
    print("Name 1;",v[firstName])
     print("Name 2;",v[lastName])
      print("Account No;",v[AccNo])
       print("balance;",v[AccBal])