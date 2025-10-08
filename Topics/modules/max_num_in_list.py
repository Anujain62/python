
from functools import reduce


# if here we exicutes this file directly so this prints __main__ otherwise this is prints file name.
print("inside max_num_in_list file :",__name__)

def minValue(a,b):
 if a<b:
  return a
 return b

def maxValue(a,b):
 if(a>b):
  return a 
 return b 

if __name__ == "__main__":
 size = int(input("enter size of the list : "))
 l = []
 print("Enter elements of list : ")
 for i in range(0,size,1):
  ele = input()
  l.append(ele)

 print(f"max value : {reduce(maxValue,l)}")
 print(f"min value : {reduce(minValue,l)}")




 













