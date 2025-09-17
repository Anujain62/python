# A class method is bound to the class and receives the class  as an implicit first argument. 
# Note -> static method can't access or modify class state and generally for utility. 
# eg. ->
# class Student:
#  @classmethod          #decorator
#  def collage(cls):
#   pass





class Person:
 name = "anonymous"

 # normal function creates new attributes for object and stores the data, here data does not stores inside the class attributes
 # def changeName(self,name):
 #  self.name = name 

 # we can change class attributes using two ways ->
 # 1) using direct class name,  
 #  syntax -> class_name.attribute_name = parameter
 # def changeName(self,name):
 #  Person.name = name

 # 2) syntax -> self.__class__.attribute_name = parameter
#  def changeName(self,name):
#   self.__class__.name = name

#  class attributes changes using class methods
 @classmethod
 def changeName(cls,name):
  cls.name = name 

  

p1 = Person()
p1.changeName("anu") 
print(p1.name)
print(Person.name) 






































