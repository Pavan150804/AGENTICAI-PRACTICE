class parent:
    def show(self):
        print("Parent function")

class child(parent):
    def show(self):
        super().show()
        print("child function")   
c = child()
c.show()


# Constructor

class Student:
    def __init__(self,name):
        self.name=name
        print("parent..")

class person(Student):
    def __init__(self,name,roll):
        print("child..")
        super().__init__(name)
        self.roll=roll
        
p = person("Pavan",121)

print(p.name)
print(p.roll)

