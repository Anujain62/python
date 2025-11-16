
n = int(input())

left=0
right=n-1 

for i in range(n):
 if(i<(n/2) and left<right):
  for j in range(0,left):
   print("*",end="")
  print("\\",end="") 
  for j in range(left+1,right):
   print("*",end="")  
  print("/",end="") 
  for j in range(right+1,n):
   print("*",end="")
  left+=1
  right-=1
 elif(i==n//2 and left==right):
  for j in range(0,left):
   print("*",end="")
  print("X",end="") 
  for j in range(left+1,n):
   print("*",end="")
  left-=1
  right+=1 
 else:  
  for j in range(0,left):
   print("*",end="")
  print("/",end="") 
  for j in range(left+1,right):
   print("*",end="")  
  print("\\",end="") 
  for j in range(right+1,n):
   print("*",end="")
  left-=1
  right+=1
 print() 

