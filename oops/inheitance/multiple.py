class Father:
    def money(self):
        print("money...")

class Mother:
    def love(self):
        print("love....")

class child(Father,Mother):
    pass


c=child()
c.love()
c.money()