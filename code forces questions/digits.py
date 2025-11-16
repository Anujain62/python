
n = int(input())
lst = []

for i in range(n):
 lst.append(int(input()))

for i in lst:
 if(i==0):
  print(0)
  continue
 while i>0:
  print(i%10,end=" ")
  i//=10
 print() 

