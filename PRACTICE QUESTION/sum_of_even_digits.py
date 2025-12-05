
num = int(input("Enter a number : "))
sum = 0
while num>0:
 temp = num%10
 if(temp%2==0):
  sum+=temp
 num//=10 

print("sum = ",sum)  