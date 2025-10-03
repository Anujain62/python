a = 89   #this is called global variable,it is used every where.


def fun():

 global a   #if we use this so, here a changes the value of global variable.
 a = 5
 print(a)


 # a=3   #this is called local variable of fun(), this is create new memory, it does not changes the value of global variable.
 # print(a)



fun()
print(a)   #it prints global variable.