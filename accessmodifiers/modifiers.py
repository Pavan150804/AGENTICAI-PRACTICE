class house:
     def __init__(self):
          self.hall="This is a public rooom"
          self._children="This is a Protected room"
          self.__bedroom="This is private room"
     
     def __access_bedroom(self):
          print(self.__bedroom)

     def show(self):
          self.__access_bedroom()
          
     def _access_children(self):
          print(self._children)
          self.__access_bedroom()
     
     def access_hall(self):
          print(self.hall)

class apt(house):
  pass 
a = apt()

a.show()
a._access_children()
     