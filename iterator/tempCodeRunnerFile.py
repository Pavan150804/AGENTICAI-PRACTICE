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