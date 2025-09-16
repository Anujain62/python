# To map  with real world scenarios,we started using object in code. 
# this is called object oriented programming.

# class -> class is a blueprint for creating objects.
# creating class -> 
#  class Student:
#   name = "anu jain"

# creating object(instance) 
# s1 = Student()
# print(s1.name)




# eg. 1 ->
# # class creation
# class Student :
#  name = "anu"
# # object creation
# s1 = Student()
# print(s1.name)

# eg. 2->
# class Car :
#  color = "blue"
#  brand = "mercedes"
# car1 = Car()
# print(car1.color)
# print(car1.brand)





# constructor (_ _init_ _ function) -> all classes have a function called __init__(), which is always executed when the object is being initiated.
# 'the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.'
# # creating class
# class Student:
#  def __init__(self,fullname):
#   self.name = fullname
# # creating object
# s1 = Student("karan")
# print(s1.name) 


# eg. 1 ->
class Student:
 # default constructor
 def __init__(self):
  pass
 # parameterized constructor
 def __init__(self,fullname): #self is a parameter,here we can change the name of the self parameter, it is point to it-self, it is compulsary, it is pints to the address of the object.
  self.name = fullname
  print("adding new student in Database...")
s1 = Student("ANU")
print(s1.name)
s2 = Student("Akku")
print(s2.name)








