
num = int(input("enter a number :"))
n = num
fact = 1
while num>0:
 fact*=num 
 num-=1

print("factorial of {} is {}".format(n,fact))