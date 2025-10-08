
# when we import whole file so we can exicute every function or every line of code.
# import max_num_in_list 



# if we import any specific function so we can just exicutes only this function.
from max_num_in_list import maxValue
from functools import reduce


# if we exicutes this file directly so this file prints __main__ and max_num_in_list file prints file name max_num_in_list.
print("inside main file : ",__name__)

size = int(input("enter size of the list : "))
l = []
print("Enter elements of list : ")
for i in range(0,size,1):
 ele = input()
 l.append(ele)

print(f"max value : {reduce(maxValue,l)}")

