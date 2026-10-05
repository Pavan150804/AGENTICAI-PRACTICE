myset1=set()
print(myset1)
set1 = {1,2,3,4,1,0}
print(set1)
set1.add(10)
print(set1)
set1.update([7,8,9,1])
print(set1)
list1=[1,2,3,4,6,6]
unique=set(list1)
print(unique)
unique.remove(1) # if element present removes it and if not present throws the error
unique.discard(10) # if element present removes it and if not present dont throw the error
print(unique)
unique.pop() #unordered
print(unique)
