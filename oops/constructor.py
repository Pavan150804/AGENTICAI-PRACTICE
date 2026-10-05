class person:
    def __init__(self):
        print("Haiii..")

p =person()

class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print("Constructor")
    def hai(self):
        print(self.name)
        print(self.id)
s = student("Pavan",121)
s.hai()


