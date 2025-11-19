
n = int(input())

ans = []
for i in range(n):
 sh,sm,eh,em=map(int,input().split())
 h = eh-sh
 m = em-sm
 if m<0:
  h-=1
  m = 60+m
 temp = [] 
 temp.append(h)
 temp.append(m)
 ans.append(temp)


for i in ans:
 for j in i:
  print(j,end=" ")
 print() 

