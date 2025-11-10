
size = int(input("enter size of list :"))
print("Enter elements of list :")
lst = []
for i in range(size):
 lst.append(int(input()))

num = int(input("Enter a number :")) 

idx = []
for i in range(size):
 for j in range(i+1,size):
  if(num == lst[i]+lst[j]):
   idx.append(i)
   idx.append(j)
   break
 if(idx):
  break
else:
 print("Sum not fount!")  

if(idx):
 print("Indices of sum : ", idx)






