
n = int(input())
lst = []
for i in range(n):
 n,m=map(int,input().split())
 temp=[]
 temp.append(n)
 temp.append(m)
 lst.append(temp)

for i in lst:
 n=i[0]
 m=i[1]

 x=min(n,m)
 y=max(n,m)

 sum=0
 for j in range(x+1,y):
  if(j%2!=0):
   sum+=j 

 print(sum)  

