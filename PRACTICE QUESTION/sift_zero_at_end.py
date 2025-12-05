

size = int(input("enter size of list :"))
print("Enter elements of list :")
lst = []
for i in range(size):
 lst.append(int(input()))

right = 0
for i in range(0,size,1):
 if(lst[i]!=0):
  lst[i],lst[right] = lst[right],lst[i]
  right+=1

print("New list :",lst) 






