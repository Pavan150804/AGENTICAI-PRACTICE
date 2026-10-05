class num:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value+ other.value

n1=num(10)
n2=num(20)

print(n1+n2)

print(str(n1))