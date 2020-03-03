#OBJECT ORIENTED PROGRAMMING
#class, object, properties, methods, inheritance

#class customer:
   # firstname='petero'

#print(customer.firstname)


#customer1=customer()
#print(customer1.firstname)

#customer2=customer()

#customer3=customer()

   # def __init__(self,firstname,lastname,age):
    #    self.firstname=firstname
     #   self.lastname=lastname
      #  self.age=age

#zaza=customer("zaza","mastigaveli",20)
#print(zaza.firstname)
#zaza.age=32
#print(zaza.age)

#    def myOutput(self):
#        print(self.firstname)

#zaza=customer("zaza","mastigaveli",20)
#zaza.myOutput()

#user input account details

class Account:
    def __init__(self,balance,customerName,accountNumner,currency):
         self.balance=balance
         self.customerName=customerName
         self.accountNumner=accountNumner
         self.currency=currency

    def myOutput(self):
        #print(self.customerName,self.accountNumner,self.currency,self.balance) not relevant as much

#zaza=Account("Kes 32,456","Zaza Mastigaveli","123456789","Kes")
#zaza.myOutput()

    
balance=input("balance")
customerName=input("C.Name")
accountNumner=input("Acc NO.")
# currency=input('KES')

account1=Account(balance,customerName,accountNumner,'KES')


account1.myOutput()