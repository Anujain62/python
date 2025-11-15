n=int(input())
lst = []
for i in range(n):
 lst.append(int(input()))

for i in range(n):
 fact=1
 for j in range(1,lst[i]+1):
  fact*=j 
 print(fact) 