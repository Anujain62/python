
n=int(input())

fact=1
for i in range(1,n+1):
 fact*=i 

count=0
while fact>0: 
 fact//=10
 count+=1

print(f"Number of digits of {n}! is ",count)
