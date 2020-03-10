firstname=input("enter your name")
secondname=input("enter your name")

print("Good morning {} {}".format(firstname,secondname))

recipientName=input("enter the name of recipient: ")
recipientPhone=input("enter phone number: ")
amount=input("enter amount: ")


print("send Ksh {} to {} of {}".format(amount, recipientName, recipientPhone))

confirm=int(input ("press '1' to proceed"))
if(confirm==1):
    balance=3000
    newBal=3000-int(amount)

print("Confirmed {} sent to {} of {}. Balance is KSH {}".format(amount, recipientName, recipientPhone, newBal)) 

