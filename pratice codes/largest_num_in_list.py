
size = int(input("enter size of the list :"))
lis = []
print("enter element :")
for i in range(0,size):
 ele = int(input())
 lis.append(ele)

largest = lis[0]
for ele in lis:
 if(largest<ele):
  largest = ele

print("largest number = ",largest)   

