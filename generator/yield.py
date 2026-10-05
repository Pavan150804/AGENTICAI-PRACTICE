def generate_num():
    num=3
    print("Beforing entering the loop....")
    while(num<10):
        print("before yield num = ",str(num))
        yield num
        num+=1
        print("after yield num = ",str(num))

gen = generate_num()

next(gen)
print("----------")
next(gen)
print("----------")
next(gen)

for i in gen:
    print(i)

