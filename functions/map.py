def square(a):
      print(a*a)
list(map(square,[1,2,3,4]))

num= list(map(lambda a : a*a,[1,2,3,4])) 

res=map(lambda x: x+1,[1,2,3,4,5])
for i in res:
      print(i)
