
n,q = map(int,input().split())

lst = list(map(int,input().split()))
ans = []
for i in range(q):
 l,r = map(int,input().split())
 sum = 0
 for j in range(l-1,r):
  if j>r:
   break
  else:
   sum+=lst[j]
 ans.append(sum) 

for i in ans:
 print(i)

