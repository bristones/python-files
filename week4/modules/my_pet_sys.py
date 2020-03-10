from bulldog import Bulldog
from dog import Dogs
from germanshepherd import GermanShepherd
from pet import Pets
from pitbull import Pitbull



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

