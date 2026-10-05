class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
       return f"{self.name} earns {self.salary}"
    

e = Employee("Pavan", 50000)

print(e)