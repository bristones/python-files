pi=3.142
radius=float(input("enter the radius"))
circ=2*pi*radius
print(circ)

print("area=2*pi*radius", "=", "2*pi*{}",circ)


mystr='circumference=2*{}*{}'.format(radius,radius)
print(mystr)
