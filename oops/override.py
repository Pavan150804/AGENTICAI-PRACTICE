class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("class B")

obj = B()
obj.show()


