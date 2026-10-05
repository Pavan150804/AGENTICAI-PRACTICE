my_dict = { "item1":1,"item2":2,"item3":3}
 
 # iteraate through keys
for i in my_dict:
    print("Keys "+i)
    print("values "+str (my_dict[i]))

# iteraate through values
for i in my_dict.values():
    print("values "+ str(i))

# iterate through key-value pairs
for i,j in my_dict.items():
    print(i+":"+str(j))
 