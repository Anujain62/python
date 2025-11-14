
size = int(input())

numbers = list(map(int, input().split()))
even = 0
odd = 0
pos = 0
neg = 0

for i in numbers:
 if i==0:
  even+=1
 if i>0:
  pos+=1
  if i%2==0:
   even+=1
  else:
   odd+=1 
 elif i<0:
  neg+=1 
  if i%2==0:
   even+=1
  else:
   odd+=1 

print("Even:",even)    
print("Odd:",odd)    
print("Positive:",pos)    
print("Negative:",neg)    
