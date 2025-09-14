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



# def sum(a,b):
#  return a+b
# print(sum(6,8))



# average of 3 numbers
# def average(a,b,c):
#  sum = a+b+c
#  return sum/3
# print(average(17,8,9))



# default parameter
def cal_prod(a=1,b=1):
 return a*b
print(cal_prod())
print(cal_prod(4,6))
















