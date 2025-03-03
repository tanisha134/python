class ParentInfo:
    def __init__(self, name, number):
        print(f"my name is {name}, & My Number Is {number}")

    def YourName(self , Number):
        self.Number = Number

        print(Number)

    @classmethod
    def MyName(LMS):
        print("hello python")

p1 = ParentInfo("Tanisha" , "01234456787")
ParentInfo.MyName()
p1.MyName()

p1.YourName("hafsa")

#Instance Method
class ClassName:
    def InstanceMethod(self):
        print("hello Instance Method")

    @classmethod
    def ClassMethod(cls):
        print("This Is Class Method")

    @staticmethod
    def staticMethod():
        print("This Is StaticMethod")



v1 = ClassName()
v1.InstanceMethod()

v1.ClassMethod()
ClassName.ClassMethod()

v1.staticMethod()
ClassName.staticMethod()
