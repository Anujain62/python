
num = int(input("enter a number : "))
n = num
newNum = 0
while n>0:
 temp = n%10
 newNum += temp**3
 n//=10

if(num==newNum):
 print("Armstrong")
else:
 print("Not Armstrong") 


