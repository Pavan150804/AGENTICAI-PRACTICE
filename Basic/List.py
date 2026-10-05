mylist=[1,2,4,4,0,"Hello",True,5.98]
emptyList=list()
mylist.append("hai") # to add  to the existing list we use append
mylist[1]=90 # updation
mylist.insert(0,10) # insert at particular index
mylist.remove(0) # remove
del mylist[3]
del mylist[4:7] # del group elements
#print(mylist.pop()) it returns and remove the last element is a list
print(mylist)
print(emptyList)
print(mylist[0])
print(mylist[-1])
print(mylist[2:5:2]) # slicing lst_items[start:stop:step]
print(mylist[::-1]) 

a="welcome"  #slicing
print(a[::-1])

