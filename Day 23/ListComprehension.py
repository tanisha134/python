#List Comprehensions
Num = [1,2,3,4,5,6,7,8,9]
for T in Num:
    print(T * 2)
Double = [ T * 2 for T in Num ]
print(Double)

Double = [ T + 2 for T in Num ]
print(Double)
Double = [ T - 2 for T in Num ]
print(Double)
Double = [ T / 2 for T in Num ]
print(Double)









