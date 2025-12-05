
lst = []
unique_list = []
size = int(input("Enter size of the list :"))
print("Enter elements of the list :")
for i in range(0,size,1):
 temp = int(input())
 lst.append(temp)

for item in lst:
 if item not in unique_list:
  unique_list.append(item)
 
print("After removing duplicates : ",unique_list)