#Binary type data

TanishaList = [1,2,3,54,5,41,2,121,255]
b =  bytes(TanishaList)
print(type(b))
#Binary type data byteArray
TanishaList1 = [1,2,3,54,5,41,2,121,255]
b1 = bytearray(TanishaList1)
print(type(b1))
b1[1] = 100
print(b1[1])