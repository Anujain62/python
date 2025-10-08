# polymorphism : operator overloading -> when the same operator is allowing to have diffrent meaning according to the context.

# operator & dunder functions -> 
# 1) addition            a+b              a.__add__(b)
# 2) subtraction         a+b              a.__sub__(b)
# 3) multiplication      a+b              a.__mul__(b)
# 4) division            a+b              a.__truediv__(b)
# 5) mod                 a+b              a.__mod__(b)
# 6) comparision         a>b              a.__gt__(b) 


# eg.->
# print(1+2) #add numbers
# print("anu "+"jain")   #concatenate
# print([1,2,3],[4,5,6])  #merge



# # operator overloading example ->
# class Complex:
#  def __init__(self,real,img):
#   self.real = real
#   self.img = img 

#  def showNumber(self):
#   print(self.real,"i +",self.img,"j")

#  # normal function
#  # def add(self,num2):
#  #  newReal = self.real + num2.real
#  #  newImg = self.img + num2.img
#  #  return Complex(newReal,newImg)

#  # tinder function
#  def __add__(self,num2):         #operator overloading
#   newReal = self.real + num2.real
#   newImg = self.img + num2.img
#   return Complex(newReal,newImg)

# num1 = Complex(2,6)
# num1.showNumber()
# num2 = Complex(3,2)
# num2.showNumber()

# # if we use normal function so we can't use + operator for adding, because it gives an error
# # num3 = num1 + num2
# # if we use normal function so use this method
# # num3 = num1.add(num2)
# # num3.showNumber()

# # if we use tinder function so we can use + operator for addition, this is called operator overloading
# num3 = num1 + num2     #operator overloading
# num3.showNumber()







# # method overloading example
# class Student:
#  def __init__(self,m1,m2):
#   self.m1 = m1 
#   self.m2 = m2 

#  def sum(self,a=None,b=None,c=None):        #sets all default values with none
#   s = 0
#   if a!=None and b!=None and c!=None:
#    s = a+b+c 
#   elif a!=None and b!=None:
#    s = a+b 
#   else:
#    s = a   
#   return s
# s1 = Student(58,68)
# print(s1.sum(5))
# print(s1.sum(5,6))
# print(s1.sum(5,6,7))






# method overriding example 
class A:
 def show(self):
  print("in A show")

class B(A):
 def show(self):       #this overrides the show function of parent class A.
  print("in B show")

a1 = B()
a1.show()





















