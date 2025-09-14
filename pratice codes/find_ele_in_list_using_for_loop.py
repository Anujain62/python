size = int(input("enter size of the list:"))
list_ele = []
print("enter elements of the list :")
i = 0
for i in range(size):
 list_ele.append(input())
target = input("enter searching element :") 
found = True
for ele in list_ele:
 if(ele == target):
  found = True
  break
 else:
  found = False
if(found):
 print(target,"is found")  
else:
 print(target,"is not found") 
