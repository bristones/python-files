from dog import Dogs

class Bulldog(Dogs):
    def __init__(self,color,size,age,sound,Nofpupies):
        super(). __init__(color,size,age)
        self.Nofpupies=Nofpupies
        self.sound=sound
    def sound(self):
        print('A bulldog sounds like i dont know')
    def Nofpupies(self):
        print('it has little, cute puppies')
    