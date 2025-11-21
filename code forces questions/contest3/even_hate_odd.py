
t = int(input())

for i in range(t):
 n = int(input())
 lst = list(map(int,input().split()))
 ans = -1

 even = 0
 odd = 0
 for x in range(n):
  if lst[x]%2==0:
   even+=1
  elif lst[x]!=0:
   odd+=1
 if even==odd:
  ans=0
 else:
  ans = abs((even-odd)//2) if (even-odd)%2==0 else -1
 print(ans)   


 



