
def equn(x,n):
 i=0
 sum=0
 while i<=n:
  if i==0:
   sum+=(x**i-1)
  else:
   sum += (x**i) 
  i+=2 
 return sum 




x,n=map(int,input().split())

print(str(equn(x,n)))