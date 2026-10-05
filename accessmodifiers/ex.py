class hi:
    def A(self):
        print("public")
    def _B(self):
        print("protected")
    def __c(self):
        print("private")

h = hi()
h.A()
h._B()
h._hi__c()