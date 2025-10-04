from functools import reduce

def maxValue(a,b):
 if(a>b):
  return a 
 return b 

size = int(input("enter size of the list : "))
l = []
print("Enter elements of list : ")
for i in range(0,size,1):
 ele = input()
 l.append(ele)

print(f"max value : {reduce(maxValue,l)}")




 













