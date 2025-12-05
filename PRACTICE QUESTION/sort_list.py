
size = int(input("Enter size of the list :"))
lst = []
print("Enter elements of the list :")
for i in range(0,size,1):
 temp = input()
 lst.append(temp)

for i in range(0,size-1,1):
 for j in range(i,size,1):
  if(lst[i]>lst[j]):
   temp = lst[i]
   lst[i] = lst[j]
   lst[j] = temp

print("Sorted list ",lst)   