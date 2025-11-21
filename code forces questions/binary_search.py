
n,q = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans = []
for i in range(q):
 x = int(input())
 left = 0
 right = n-1
 found = False
 while left<=right:
  mid = (left+right)//2
  if lst[mid]==x:
   found = True
   break
  elif lst[mid]<x:
   left = mid+1
  elif lst[mid]>x:
   right = mid-1  
 if found:
  ans.append(True)  
 else:
  ans.append(False) 

for x in ans:
 print("found" if x else "not found")
