
n = int(input())
m = n 
temp = 0
while m>0:
 x = m%10
 m//=10
 temp = temp*10 + x

if(temp==n):
 print(temp)
 print("YES")
else:
 print(temp)
 print("NO")
