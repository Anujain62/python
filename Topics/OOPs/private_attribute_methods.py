# private(like) attributes and methods -> conceptual implementation in python -> private attributes and methods are meant to be used only within the class and not accessible from outside the class 





# # by default all attributes and methods are public
# # eg. 1 ->
# class Account:
#  def __init__(self,acc_no,acc_pass):
#   self.acc_no = acc_no
#   # private decleration -> use __ before the attribute or method
#   self.__acc_pass = acc_pass   

#  def get_pass(self):
#   return self.__acc_pass    

# acc1 = Account("12345","abcde")  
# print(acc1.acc_no)  
# print(acc1.get_pass())







# eg. 2 ->
class Person:
 __name = "anu"
 def __hello(self):
  print("hello person!")

 def wecome(self):
  self.__hello() 

p1 = Person()

# print(p1.__hello())   #here we can't access directly hello method, because it is private.

p1.wecome()












