#Multiple Inheritance
class baba:
    car = "BMW"
    tk = "100 Crore"
    Home = "10 Floor"

class baba2:
    SmartPhone = "IPhone"
    AC = "Walton"
    Micropjone = "Fifine"

class baba3:
    Webcam = "Fifine K0"
    Laptop = "Walton"
    Camera = "Fifine"

class kaka(baba,baba2,baba3):

    BrokenPhone = ""
    BrokenHome = ""

k = kaka()

print(k.Laptop)
print(k.Webcam)

