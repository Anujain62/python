
n = int(input())

lst = list(map(int,input().split()))

count = 0
no_one = False
while True:
 for i in lst:
  print("i ",i)
  if i%2==0:
   i//=2
  else:
   no_one = True
   break 
 else:
  count+=1 
 if no_one:
  break 
print(count)   
