class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
c = Cat()

d.eat()
c.eat()