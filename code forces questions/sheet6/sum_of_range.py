
a,b=map(int,input().split())

sum=0
odd_sum=0
even_sum=0
if a>b:
 a,b=b,a
for i in range(a,b+1):
 if i%2==0:
  even_sum+=i
 elif i%2!=0:
  odd_sum+=i 
 sum+=i 

print(sum)   
print(even_sum)
print(odd_sum)

