list_ele = []
size = int(input("enter size of the tuple:"))
i = 0
print("enter elements of tuple : ")
while i<size:
 list_ele.append(int(input()))
 i+=1
x = int(input("enter searching element :"))

tup = tuple(list_ele)
i = 0
found = True
while i<size:
 if(tup[i] == x):
  found = True
  break
 else:
  found = False
 i+=1 
if(found):
 print(x,"is found")
else:
 print(x,"is not found") 




















