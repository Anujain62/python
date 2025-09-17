# super() method is used to access methods of the parent class. 




class Car:
 def __init__(self,type):
  self.type = type

 @staticmethod
 def start():
  print("Car started..")

 @staticmethod
 def stop():
  print("car stopped...") 

class ToyotaCar(Car):
 def __init__(self, name,type):
  super().__init__(type)                   #constructor calling
  self.brand = name
  super().start()                   # function calling

car1 = ToyotaCar("prius","electric")
print(car1.type)
























