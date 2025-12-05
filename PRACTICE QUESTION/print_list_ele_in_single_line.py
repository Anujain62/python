size = int(input("enter size of the list:"))
print("enter elements of the list:")
list_ele = []
i = 0
while i<size:
 list_ele.append(input())
 i+=1
print("elements of the list :") 
for ele in list_ele:
 print(ele,end=" ")