
size = int(input("enter size of list :"))
lst = []
print("Enter strings of the list :")
for i in range(size):
 lst.append(input())


print("Common characters are :")
for ch in lst[0]:
 for word in lst[1:]:
  if(ch not in word):
   break
 else:
  print(ch,end=" ") 
