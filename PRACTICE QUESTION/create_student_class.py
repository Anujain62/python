# create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average


class Student:

 # # marks passed from diffrent parameters
 # def __init__(self,name,phy,chem,math):
 #  self.name = name
 #  self.phy = phy
 #  self.chem = chem
 #  self.math = math 

 # marks passed as list 
 def __init__(self,name,marks):
  self.name = name
  self.marks = marks

 def average(self):
  sum = 0
  for val in self.marks:
   sum+=val
  print("Hii",self.name,"average =",sum/3)

s1 = Student("anu",[98,85,70])  
s1.average()

s1.name = "akku"
s1.average()











