# To map  with real world scenarios,we started using object in code. 
# this is called object oriented programming.

# class -> class is a blueprint for creating objects.
# it contains attributes/variable and behaviour/method/function.
# creating class -> 
#  class Student:
#   name = "anu jain"

# creating object/instance
# s1 = Student()
# print(s1.name)

# class method/function calling - 
# 1) class_Name.method_Name(object_name)
# 2) object_name.method_name


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





# constructor (__init__ function) -> all classes have a function called __init__(), which is always executed when the object is being initiated.
# 'the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.'
# # creating class
# class Student:
#  def __init__(self,fullname):
#   self.name = fullname
# # creating object
# s1 = Student("karan")
# print(s1.name) 

# # eg. ->
# class Student:
#  # default constructor
#  def __init__(self):
#   pass
#  # parameterized constructor
#  def __init__(self,fullname): #self is a parameter,here we can change the name of the self parameter, it is point to it-self, it is compulsary, it is pints to the address of the object.
#   self.name = fullname
#   print("adding new student in Database...")
# s1 = Student("ANU")
# print(s1.name)
# s2 = Student("Akku")
# print(s2.name)





# types of methods -> intance method, class method, static method
# 1)  # instance method -> It's a regular method inside a class.It always takes self as the first parameter.It can access or modify instance variables (those defined using self.variable).You call it on an object, not on the class itself.
# types of instance method -> access methods(it gets the values), mutator methods(it sets the values)

class Student:
 school = "Telusko"   #class variable

 def __init__(self,m1,m2,m3):
  self.m1 = m1   #instance variable
  self.m2 = m2   #instance variable 
  self.m3 = m3   #instance variable

 def avg(self):       # instance method
  return (self.m1+self.m2+self.m3)/3 
 
 @classmethod
 def getSchool(cls):     #class method
  return cls.school
 
 @staticmethod
 def info():          #static method
  print("This is student class.")
 
s1 = Student(34,56,78)  
s2 = Student(67,88,98)
print(s1.avg())   #instance method calling
print(Student.getSchool())   #class method calling
Student.info()        #static method calling





















