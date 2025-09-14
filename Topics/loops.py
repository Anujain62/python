# loops are used to repeat instructions.
# iteration -> one time whole loop code runs
# iterator -> variable name whose used for condition

# 1) while loop -> 
# while condition:
#  some work

# break -> used to terminate the loop when encountered
# continue -> terminates exicution in the current iteration and continues execution of the loop with next iteration



# i = 5
# while i>0 :
#  print("hello")
#  i -= 1


# i = 0
# while i<=5:
#  if(i==3):
#   break
#  print(i)
#  i+=1


# i=0
# while i<=5:
#  if(i==3):
#   i+=1
#   continue
#  print(i)
#  i+=1



# loops are used for sequential traversal
# for loop ->
# for ele in list:
#  some work

# for loop with else
# here else is work while whole loop is exicute,if we break the loop at specific condition so this else does not work
# for ele in list:
#  some work
# else:
#  work when loop ends 


# num = [1,2,3,4,5]
# for val in num:
#  print(val)

# tup = (1,2,3,4,5,6)
# for val in tup:
#  print(val)


# str = "apnacollage"
# for char in str:
#  if(char == "o"):
#   print("o found")
#   break
#  print(char)
# else:
#  print("END") 





# range -> ragnge function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. 
# it excludes the last number
# range(start?,stop,step?)
# here starting index and step size(idex number for increasing) is optional and stop condition is compusary

# list_ele = [1,2,3,4,5,6]
# 1)
# for idx in range(len(list_ele)):
#  print(list_ele[idx])

# 2) it exclude last index
# for idx in range(1,3):
#  print(list_ele[idx])

# 3) it increase index by 2  
# for idx in range(1,6,2):
#  print(list_ele[idx])





# pass statement -> pass is a null statement that does nothing. it is used as a placeholder for future code.
# for ele in range(10):
#  pass

# for i in range(5):
#  pass
# if(i>5):
#  pass
# print("some useful work")










