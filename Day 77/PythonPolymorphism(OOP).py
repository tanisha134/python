#Polymorphism is a term used to refer to an object's ability to take on multiple forms.
from idlelib.pyshell import ModifiedUndoDelegator


#Polymorphism

class Vehicle:
    def __init__(self, Model, Brand, Component):
        self.Model = Model
        self.Brand = Brand
        self.Component = Component




class Plane(Vehicle):
    pass

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass


p1 = Plane("Tanisha420", "Tanisha", "All Component")

c1 = Car("BMW", "E221", "Main Component")

b1 = Bike("RTR", "001", "Component")

print(p1.Brand, p1.Model, p1.Component)

print(c1.Component, c1.Brand, c1.Model)

print(b1.Model, b1.Brand, b1.Component)

