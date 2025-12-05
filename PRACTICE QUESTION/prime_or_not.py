
num = int(input("enter a number :"))
is_prime = False
for i in range(2,num,1):
 if(num%i==0):
  print("number is not prime")
  break
else:
 print("number is prime")  