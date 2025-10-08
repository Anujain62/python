class Student:       #outer class
 def __init__(self,name,rollNo):
  self.name = name 
  self.rollNo = rollNo
  self.lap = self.Laptop()

 def show(self):
  print(self.name,self.rollNo)
  self.lap.show()

 class Laptop:       #inner class
  def __init__(self):
   self.brand = "HP"   
   self.cpu = "i5"
   self.ram = 8
  def show(self):
   print(self.brand,self.cpu,self.ram) 

s1 = Student("Navin",2)
s2 = Student("Jenny",3)
s1.show()

lap1 = s1.lap
lap2 = s2.lap

print(lap1.brand)
print(lap2.brand)
