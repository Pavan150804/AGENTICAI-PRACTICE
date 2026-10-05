def hai():
    return "haii.."
def hello(h):
    return h()
print(hello(hai))

def h():
    return "h"
def j(fun):
    print(fun())
j(h)

def child(a,b):
    return(a+b)
def parent(sub,c,d):
    return(sub(c,d))
print(parent(child,10,20))
   
