
t = int(input())

for i in range(t):
 n = int(input())
 lst = list(map(int,input().split()))
 small = float('inf')
 for j in range(n-1):
  for k in range(j+1,n):
   temp = lst[j]+lst[k]+(k-j)
   if temp<small:
    small=temp
 print(small)   
