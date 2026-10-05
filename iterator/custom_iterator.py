class MyNumbers:
#    def __init__(self):
#        self.data = [10, 20, 30]
   def __iter__(self):
       return iter([1,2,3,4])  # returns a built-in list iterator.
nums = MyNumbers()

for n in nums:
   print(n)
 
print(" -----------------")

class my_iterator:
    def __init__(self,data,index):
        self.data=data
        self.index=index
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if(len(self.data)>self.index):
            value= self.data[self.index]
            self.index+=2
            return value
        else :
            raise StopIteration

my_iterable = my_iterator([5,4,3,2,1],0)
for item in my_iterable:
    print(item)


print("-----------------------")

class Count3:
    def __init__(self,num,range):
        self.num = num
        self.range= range

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.range:
            value = self.num
            self.num += 2
            return value
        raise StopIteration

c = Count3(1,10)
for item in c:
    print(item)