
num = int(input("enter a number :"))
is_prime = True
for i in range(2,num):
 if(num%i == 0):
  is_prime = False
  break

print(num,"is prime?",is_prime) 


