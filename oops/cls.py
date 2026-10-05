class Student:
    name="vamsi"
    id=0

    def setvalues(self,name,id):
        self.name=name
        self.id=id
        
    def getValues(name):
        print("im a student",name)
        print("im a student",Student.name)
        
s1 = Student()
s2 = Student()

s1.setvalues("pavan",123)
s2.setvalues("ravi",456)

print(s1.name)
print(s1.id)

print(s2.name)
print(s2.id)

Student.getValues("rahul")
Student.getValues("kiran")


