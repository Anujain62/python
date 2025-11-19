
n = int(input())
lst  =[]
for i in range(n):
 a,b=map(int,input().split())
 power = a**b
 ans = power%10
 lst.append(ans)

for i in lst:
 print(i)
