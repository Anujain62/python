
n = int(input("Enter number of rows : "))
for i in range(0,n,1):
 for j in range(0,i+1,1):
  if(j==0):
   print("1",end="")
  elif(j==i): 
   print("1",end="")
  else:
   print(i,end="")
 print()  
