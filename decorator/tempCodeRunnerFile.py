def security(fun):
    def wrapper(*args):
        print("before")
        result=fun(*args)
        print("after")
        return result
    return wrapper

@security
def hai(a,b):
    return a+b
print(hai(10,20))