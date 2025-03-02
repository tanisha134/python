#Parameterized Constructor

class parentInfo:

    def TanishaSFamily(self,name,age):
        print(f"my name is {name} ,my age is {age}")

p1 = parentInfo()
p1.TanishaSFamily("tanisha",  12)
p1.TanishaSFamily("hablu",  91)
p1.TanishaSFamily("hafsa",  7)

#Constuctor

class parentInfo1:
    def __init__(self ,name, number):
        print(f"my name is {name} , & My Number is {number} ")

p2 = parentInfo1("hafsa","012345565456")

