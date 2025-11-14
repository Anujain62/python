# Given two numbers a
#  and b
# . You have to answer with "YES" if there is a non-empty interval consisting of numbers from l
#  to r
#  (l,l+1,l+2,...,r
# ) with a odd numbers and b even numbers, or "NO" otherwise.

# Input
# Only one line containing two numbers a
#  and b
#  (0≤a,b≤100
# )the number of odd numbers and the number of even numbers in the interval respectively.

# Output
# Print "YES" or "NO" as described in the statement.






a,b = map(int,input().split())
n = a+b
if(n==0):
 print("NO")
elif(n%2==0):
 if(a==b):
  print("YES") 
 else:
  print("NO") 
else:
 half=n//2
 if((half+1==a and half==b) or (half==a and half+1==b)):
  print("YES")  
 else:
  print("NO") 