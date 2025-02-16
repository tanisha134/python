#Set Method
#Add() = Adds an element to the set
#Clear() = Removes all the elements from the set
#Copy() = Returns a copy of the set
#Difference() = Returns a set containing the difference between two or more sets
#Difference Update() =Removes the items in this set that are also included in another,specified set
#Discard() = Removes the specified item
#Intersecion() = Returns a set,that is the intersection of two other sets
#Intersecion Update() = Removes the items in this set that are not present in order,specified set(s)

#Set exercise
fruits = {"Apple","Banana","Cherry"}
if "Apple" in fruits:
    print("yes Apple is in")

fruits2 = {"Apple","Banana","Cherry"}
fruits2.add("Kiwi")
print(fruits2)
