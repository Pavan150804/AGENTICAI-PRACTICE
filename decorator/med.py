def mydec(n):
    def wrapper(s):  
        print("before")
        n(s)                #n=greet
        print("after")
    return wrapper

@mydec
def greet(name):
    print ("hello"+name)

greet("pavan")