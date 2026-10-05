from functools import reduce
def mul(x,y):
    return x * y
res=reduce(mul,[1,2,3,4])
print(res)

print(reduce(lambda x,y:x+y ,[1,2,3,4]))