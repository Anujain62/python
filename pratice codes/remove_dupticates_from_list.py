
size = int(input("enter size of list :"))
print("Enter elements of list :")
lst = []
for i in range(size):
 lst.append(int(input()))

tempLst = []
for i in range(size):
 if(lst[i] not in tempLst):
  tempLst.append(lst[i])

print("After removing duplicates : ",tempLst)

