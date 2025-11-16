
lst = []

while True:
 n,m = map(int,input().split())
 if n<=0 or m<=0:
  break
 temp = []
 temp.append(n)
 temp.append(m)
 lst.append(temp)

for i in lst:
 n=i[0]
 m=i[1]

 x=min(n,m)
 y=max(n,m)

 sum=0
 for i in range(x,y+1):
  sum+=i 
  print(i,end=" ")
 print(f"sum ={sum}") 


 
