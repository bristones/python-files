class Pets:
    dogs=[]
    def __init__(self,dogs):
        self.dogs=dogs

class Dogs:
    def __init__(self,color,size,age,):
        self.color=color 
        self.size=size
        self.age=age

    def bark(self,barkingsound):
        self.barkingsound=barkingsound

    def eat(self,food):
        self.food=food 

class GermanShepherd(Dogs):
    def speed(self):
        print('runs swiftly') 

class Bulldog(Dogs):
    def __init__(self,color,size,age,sound,Nofpupies):
        super(). __init__(color,size,age)
        self.Nofpupies=Nofpupies
        self.sound=sound
    def sound(self):
        print('A bulldog sounds like i dont know')
    def Nofpupies(self):
        print('it has little, cute puppies')
    

class Pitbull(Dogs):
    def ears(self):
        print('it has slepy ears')


gs=GermanShepherd("blue","small","3years")
bd=Bulldog("brown","large","2years",'A bulldog sounds like i dont know','it has little, cute puppies')
pb=Pitbull("white","big","5years")

#print(pb.age)


#print(pb.age,pb.color,pb.size)
print("a Bulldog of",bd.age,'is color',bd.color,"of",bd.size,"size and", bd.sound, "not forgetting", bd.Nofpupies)



myDogList=[gs,bd,pb]
Pets.dogs=myDogList

#for x in Pets.dogs:
#    print(x.age)

