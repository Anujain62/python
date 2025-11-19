
n = int(input())
x  = int(input())
lst = []
for i in range(n):
 lst.append(int(input()))

for i in lst:
 if i>=x:
  print("YES") 
 else:
  print("NO") 