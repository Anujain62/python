# block of statements that perform a specif task.
# 1) function definition
# def fun_name(param1,param2,...):
#  some work
#  return value
# 2) function call 
# fun_name(arg1,arg2,...)

# types of functions
# 1) built-in functions -> print() function ends with new line(\n),if we wants to print some lines in same line so we can assign (end = " "), eg.-> print("anu",end=" ")   print("jain"), output-> anu jain
# 2) user define function


# default parameters -> assigning a default value to parameter, which is used when no argument is passed.
# we assigning default values from ends to start



# parameterized function
# def sum(a,b):
#  return a+b
# print(sum(6,8))



# average of 3 numbers
# def average(a,b,c):
#  sum = a+b+c
#  return sum/3
# print(average(17,8,9))



# default parameter
# def cal_prod(a=1,b=1):
#  return a*b
# print(cal_prod())
# print(cal_prod(4,6))



# 2 values return by function
# def add_sub(x,y):
#  sum = x+y
#  sub = x-y 
#  return sum,sub
# sum,sub = add_sub(5,4)
# print(f"sum = {sum}\nsub = {sub}")




# pass list to a function
def count(lst):
 even = 0
 odd = 0
 for i in lst:
  if i%2==0:
   even+=1
  else:
   odd+=1
 return even,odd   
lst = [20,25,14,19,16,24,28,47,26]
even,odd = count(lst)
print(f"Event = {even} and Odd = {odd}")




# types of arguments - actual arguments
# types of actual arguments - position,keyword,default,variable length

# # a and b is called formal/actual arguments
# def add(a,b):
#  c=a+b
#  print(c)
# add(5,6) 


#1) position arguments - here values assigns according to position.
# def person(name,age):
#  print(name)
#  print(age)
# person("anu jain",20)


#2) keyword arguments - here values are assigns according to the variable/keyword name.
# def person(name,age):
#  print(name)
#  print(age)
# person(age=20,name="anu jain")   


#3) default arguments - here we sets default value means if any contion user does not passed any parameter and we are set this parameter so here use this default value.
# def person(name,age=20):
#  print(name)
#  print(age)
# person("anu jain")   


# 4) variable length - here first parameter stored 1st value and 2nd parameter stored whole values(remaining values)
# single * accepts only remaining values. 
# def sum(a,*b):
#  c=a
#  for i in b:
#   c+=i
#  print(c) 
# sum(5,6,34,23)

# double ** accepts all remaining keys and values.
# def person(name,**data):
#  print(name)
#  for i,j in data.items():
#   print(i,j)
# person("anu",age = 20,city= "jabalpur",number = 983245) 







