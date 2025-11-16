
n,a,b = map(int,input().split())

sum=0
for i in range(n+1):
 temp = 0
 x = i
 if(i<10):
  temp=i 
 else:
  while i>0:
   temp+= i%10
   i//=10
 if(a<=temp<=b):
  sum+=x


print(sum)