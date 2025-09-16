# when class attribute and object attribute name is same so here precidence of object attribute is higher as compared to class attributes.

class Student:
 collage_name = "ABC Collage"    # class attributes
 name = "anonymous"
 def __init__(self,name,marks):
  self.name = name         # object attributes
  self.marks = marks

s1 = Student("anu","85")

print(s1.name)          # access of object attributes

print(Student.collage_name)           # access of class attributes















