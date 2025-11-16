
n = int(input())
lst = []
for i in range(n):
 lst.append(int(input()))

for i in lst:
 temp = []
 while i>0:
  x = i%2
  i//=2
  temp.append(x)

 count = 0
 for j in temp:
  if(j==1):
   count+=1

 sum=0
 x = 1
 while count>0:
  sum += x 
  x*=2
  count-=1

 print(sum) 
