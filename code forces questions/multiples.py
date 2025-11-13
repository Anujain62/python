# Given two numbers A and B. Print "Multiples" if A is multiple of B or vice versa. Otherwise print "No Multiples".Given two numbers A and B. Print "Multiples" if A is multiple of B or vice versa. Otherwise print "No Multiples".   


a,b = map(int,input().split())
if(a%b==0 or b%a==0):
 print("Multiples")
else:
 print("No Multiples") 