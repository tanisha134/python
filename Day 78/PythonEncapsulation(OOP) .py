#Encapsulation
class Parent:
    def __init__(self,Name,  FatherName):
        self.__Name = Name
        self.FatherName = FatherName
        print(self.__Name)

p1 = Parent("tanisha","parvej")

print(p1.Name)

