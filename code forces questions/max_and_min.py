# Given two numbers A and B. Print "Multiples" if A is multiple of B or vice versa. Otherwise print "No Multiples".

a,b,c = map(int,input().split())

max=0
min=0
if(a>b and a>c):
 max=a
elif(b>c):
 max=b 
else:
 max=c 

if(a<b and a<c):
 min=a
elif(b<c):
 min=b
else:
 min=c

print(min,max)


