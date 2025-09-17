# we use @property decorator on any method in the class to use the method as a property. 



class Student:
 def __init__(self,phy,chem,math):
  self.chem = chem
  self.phy = phy 
  self.math = math

 @property
 def percentage(self):
  return str((self.phy+self.math+self.chem)/3) + "%"


stu1 = Student(98,97,95)
print(stu1.percentage)  
  
stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)   

# here marks of physics was changed but percentage does not change. here we can make a new method for solving this problem. but used property decorator.
# print(stu1.percentage)   

































