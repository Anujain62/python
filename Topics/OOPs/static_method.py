# methods that don't use the self parameter(work at class level).
# class Student:
#  @staticmethod    #decorator
#  def collage():
#   print("ABC Collage")

# 'Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,without permanently modifying it.'  





class Student:
 def __init__(self,name,marks):
  self.name = name
  self.marks = marks

 @staticmethod
 def hello():            #static method
  print("hello") 
  
 def average(self):
  sum = 0
  for val in self.marks:
   sum+=val 
  return sum/3

s1 = Student("anu",[98,80,70])  
s1.hello()
print(s1.average())






















