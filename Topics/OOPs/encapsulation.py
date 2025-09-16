# wrapping data and functions into  a single unit (object).



class Student:
 collage_name = "ABC Collage"
 def __init__(self,name,marks):
  self.name = name 
  self.marks = marks

 def welcome(self):
  print("welcome student",self.name) 

 def get_marks(self):
  return self.marks 
 
s1 = Student("anu",85)
s1.welcome()  
print(s1.get_marks())















