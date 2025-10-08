# when one class(child/derived) derives the properties and methods of another class(parent/base)

# types -> 1) single inheritance  2) multi-level inheritance (this creates method resolution order(MRO), it starts travers from left to right(means if class c inherite class a and class b and class c called super().__init__() method if both class are contains __init__() method so class c prefer to __init__() method of class a because class a is present left side.))  3) multilevel inheritance

# when you create object of sub-class it will  call init of sub class first, if you have call super then it will first call init of super class then call init of sub class.


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


















