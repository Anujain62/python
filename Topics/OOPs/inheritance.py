# when one class(child/derived) derives the properties and methods of another class(parent/base)

# types -> 1) single inheritance  2) multi-level inheritance  3) multilevel inheritance


# # eg. -> single inheritance
# class Car:
#  color = "black"
#  @staticmethod
#  def start():
#   print("Car started..")

#  @staticmethod
#  def stop():
#   print("car stopped...") 

# class ToyotaCar(Car):
#  def __init__(self,name):
#   self.name = name

# car1 = ToyotaCar("fortuner")  
# car2 = ToyotaCar("prius")
# print(car1.name)
# print(car1.color)
# car1.start()







# # eg. -> multi-level inheritance
# class Car:
#  @staticmethod
#  def start():
#   print("Car started..")

#  @staticmethod
#  def stop():
#   print("car stopped...") 

# class ToyotaCar(Car):
#  def __init__(self,brand):
#   self.brand = brand

# class Fortuner(ToyotaCar):
#  def __init__(self, type):
#   self.type = type

# car1 = Fortuner("diesel")
# car1.start()







# # eg. -> multiple inheritance
# class A:
#  varA = "welcome to class A"

# class B:
#  varB = "wlcome to class B" 

# class C(A,B):
#  varC = "welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


















