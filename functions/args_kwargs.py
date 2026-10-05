def fun(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)
fun(1,2,3,4,5)

def fun1(**hai):
    for key,value in hai.items():
        print(key,value)
    print(hai)
fun1(a=2,b=3,c=4)

def fun2(*args,**kwargs):
    print(args,kwargs)
fun2(1,2,3,a=10,b=20)


