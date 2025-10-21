
n = int(input("Enter the number of cases :"))
print("Enter elements of each case : ")
lst = []
for i in range(n):
 templst = []
 for j in range(2):
  temp = int(input())
  templst.append(temp)
 lst.append(templst) 
newLst = []
carry = 0
preCarry = 0
for i in range(n):
 x = int(str(lst[i][0])[::-1])
 y = int(str(lst[i][1])[::-1])
 sum = 0
 while(x>0 and y>0):
  tempX = x%10
  tempY = y%10
  x//=10
  y//=10
  tempSum = tempX+tempY+preCarry
  if(tempSum>=10):
   carry = tempSum//10
   tempSum = tempSum%10
  else:
   carry = 0 
  sum = sum*10 + tempSum 
  preCarry = carry
 if(preCarry!=0):
  sum = preCarry 
 if(x>0):
  while(x>0):
   sum = sum*10 + x%10 
   x//=10
 elif(y>0):
  while(y>0):
   sum = sum*10 + y%10
   y//=10
 newLst.append(sum)    

print(newLst)

