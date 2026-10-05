def mydec(fun):
    def wrapper():
        print("Before")
        fun()
        print("After")  
    return wrapper  #greet = wrapper because mydec() returns wrapper.
@mydec
def greet():
    print("Hello")
greet() 

print("--------------")

def hello():
    print("Hello")

def get_function():
    return hello

x=get_function()
print(x)
print(hello) 

# In Python, functions are objects, so when you print a function without calling it, Python prints the function object representation, 
# which includes its memory address (technically the object's identity).
