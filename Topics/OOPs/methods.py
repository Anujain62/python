# methods are functions that belongs to objects.
# # create class
# class Student:
#  # constructor
#  def __init__(self,name):
#   self.name = name
#  # method 
#  def hello(self):
#   print("hello",self.name) 
# # creating object
# s1 = Student("anu")
# s1.hello()



class Student:
 collage_name = "ABC Collage"
 def __init__(self,name,marks):
  self.name = name 
  self.marks = marks

 # self is important in every menthod, otherwise it give error
 def welcome(self):
  print("welcome student",self.name) 

 def get_marks(self):
  return self.marks 
 
s1 = Student("anu",85)
s1.welcome()  
print(s1.get_marks())













