class grandfather:
    def hai(self):
        print("gf hai...")
class parent(grandfather):
    def hello(self):
        print("parent hello...")
class child(parent):
    def bye(self):
        print("child bye....")


gf=grandfather()
gf.hai()

p=parent()
p.hai()
p.hello()

c=child()
c.hai()
c.hello()
c.bye()



