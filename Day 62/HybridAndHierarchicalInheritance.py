#Hybrid And Hierarchical Inheritance
class baba:
    car = "BMW"
    tk = "100 Crore"
    Home = "10 Floor"

class Son1(baba):
    SmartPhone = "IPhone"
    AC = "Walton"
    Microphone = "Fifine"

class Son2(Son1):
    Webcam = "Fifine K0"
    Laptop = "Walton"
    Camera = "Fifine"

class Son3(Son2):

    BrokenPhone = ""
    BrokenHome = ""

class Son4(Son3):

    pc = ""
    Books = ""

k = Son4()
print(k.BrokenHome)
