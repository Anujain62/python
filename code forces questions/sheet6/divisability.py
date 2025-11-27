
a,b,x=map(int,input().split())
sum=0
if a>b:
 a,b=b,a
for i in range(a,b+1):
 if i%x==0:
  sum+=i

print(str(sum))  