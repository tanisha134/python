#Iterator
list = [1,2,3,4,5,"Tanisha","Jannatul","Hafsa"]

#for t in list:
#   print(t)

e = iter(list)

print(e.__next__())
print(next(e))
