num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
for i in range(num1,num2,1):
 for j in range(2,i,1):
  if(i%j==0):
   break
 else:
  print(i) 