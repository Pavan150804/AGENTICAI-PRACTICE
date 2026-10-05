
def security(fun):
    def wrapper(**kwargs):
        print("Before Security")
        print(f"name={kwargs["name"]}, age={kwargs["age"]}")
        fun(**kwargs)
        print("After Security")
    return wrapper

@security
def create_user(name, age):
    print(f"Creating User: {name}, {age}")
    print("creating user: " ,name,age)
create_user(name="Ravi", age=25)


def secure(fun):
    def wrapper(**kwargs):
        secured_data={}
        for i,j in kwargs.items():
            print("before :" ,j)
            secured_data[i]=j+"security"
        print("connection to the db: ",secured_data)
        fun(**kwargs)
    return wrapper

@secure
def create(user,token):
    print(user,token)
create(user="admin",token="123_")


