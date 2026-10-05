from abc import ABC,abstractmethod

class printclass(ABC):
    @abstractmethod
    def printfun(self):
        pass

class hp_printer(printclass):
    def printfun(self):
        print("this is a hp printer")

class canon_printer(printclass):
    def printfun(self):
        print("this is a canon printer")

class win_printer:
    def printvendor(self,obj):
        obj.printfun()


hp = hp_printer()
cn =canon_printer()
wp = win_printer()
wp.printvendor(hp)
wp.printvendor(cn)