# del keyword -> used to delete object properties or object itself.



class Student:
 def __init__(self,name):
  self.name = name

s1 = Student("anu")  

# #perty deletion
# print(s1.name)
# del s1.name
# print(s1.name)       #it gives error because name attribute was deleted


# # object deletion
# print(s1)
# del s1 
# print(s1)           #it gives error because here s1 object was deleted



















