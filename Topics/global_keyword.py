# a = 89   #this is called global variable,it is used every where.

# def fun():

#  global a   #if we use this so, here a changes the value of global variable.
#  a = 5
#  print(a)

#  # a=3   #this is called local variable of fun(), this is create new memory, it does not changes the value of global variable.
#  # print(a)

# fun()
# print(a)   #it prints global variable.





a = 10
b=20
c=30
def something():
 a = 9
 # x=globals()          #it returns access of all global variable
 # x =globals()['a']   #we can specify global variable name.
 globals()['a'] = 15   #this change value of global variable without effecting local variable.
 print("in fun ",a)
something() 
print("outside fun ",a)


