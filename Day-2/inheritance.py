class super_class:
    name = ""
    def eat(self):
        print("I can eat")

class Dog(super_class):
    def display(self):
        print("My name is ", self.name)

labrador = Dog()
labrador.name = "Manikandan"
labrador.eat()
labrador.display()


#Method Overiding

class Animals:
    name = ""
    def eat(self):
        print("I can eat")

class Dogg(Animals):
    def eat(self):
        print("Manikandan")

animal = Dogg()
animal.eat()

#super method

class Animals:
    name = ""
    def eat(self):
        print("I can eat")

class Dogg(Animals):
    def eat(self):
        super().eat()
        print("Manikandan")

animal = Dogg()
animal.eat()

#multiple Inheritance

class superClass1:
    def mammal(self):
        print("Mammals")

class superClass2:
    def winged(self):
        print("Winged animal")

class Bat(superClass1, superClass2):
    def bat(self):
        print("bat")
    pass

b1 = Bat()
b1.bat()
b1.mammal()
b1.winged()

#multilevel inheritance

class superclass:
    def supermethod(self):
        print("super class")
class derivedclass1(superclass):
    def derivedmethod1(self):
        print("derivedclass1")
class derivedclass2(derivedclass1):
    def derivedmethod2(self):
        print("derivedclass2")

d2 = derivedclass2()
d2.supermethod()
d2.derivedmethod1()
d2.derivedmethod2()

class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2:
    def info(self):
        print("Super Class 2 method called")

class Derived(SuperClass1, SuperClass2):
    pass

d1 = Derived()
d1.info()  

