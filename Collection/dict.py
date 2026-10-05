myDict=dict()
myDict1={}
print(myDict)
print(myDict1)

newdict={1:"hai",2:"hello",3:"bye"}
print(newdict)
print(newdict[3])
print(newdict.get(4,"kiran")) #if key is present it gives the value or it gives the default value
newdict[4]="kiran" #adding a new key-value pair
newdict[2]="helo" #updating the value using key
print(newdict)
del newdict[4] # delete
print(newdict)