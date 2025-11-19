

import math
n = int(input())

ans = []

for i in range(n):
 x,y = map(int,input().split())
 ans1 = math.gcd(x,y)
 ans2 = (x*y)//ans1
 tempLst = []
 tempLst.append(ans1)
 tempLst.append(ans2)
 ans.append(tempLst)


for i in ans:
 for j in i:
  print(j,end=" ")
 print() 

 