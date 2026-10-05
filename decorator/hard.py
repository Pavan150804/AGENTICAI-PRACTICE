def addsecurity(fun):
    def wrapper(*args):
        print("before security")
        fun(*args)
        print("after security")
    return wrapper
    
@addsecurity
def adddata(*args):
    print("connecting to the db",*args)

adddata(1,2,3,4,5,5)
adddata([1,2,4,55,5])

def mysecurity(fun):
    def wrapper(*args):
        secured_params=[]
        for item in args:
            print("before "+item)
            secured_params.append(item+"security")
        print("after ",secured_params)
        fun(secured_params)
    return wrapper


@mysecurity
def postdb(p):
    print("connected to db",p)
postdb("hai")

@mysecurity
def postdb2(p,q):
    print("connected to db",p,q)
postdb("hai","helllo")


