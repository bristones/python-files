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
    def sound(self):
        print('A bulldog sounds like i dont know')


class Pitbull(Dogs):
    def ears(self):
        print('it has slepy ears')


gs=GermanShepherd("blue","small","3years")
bd=Bulldog("brown","large","2years")
pb=Pitbull("white","big","5years")

#print(pb.age)


#print(pb.age,pb.color,pb.size)
print("a pitbull of",pb.age,'is color',pb.color,"of",pb.size,"size and...............")
pb.ears()


myDogList=[gs,bd,pb]
Pets.dogs=myDogList

for x in Pets.dogs:
    print(x.age)

