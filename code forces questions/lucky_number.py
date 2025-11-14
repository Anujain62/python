# A number of two digits is lucky if one of its digits is divisible by the other.

# For example, 39, 82, and 55 are lucky, while 79 and 43 are not.

# Given a number between 10 and 99, determine whether it is lucky or not.

# Input
# Only one line containing a single number N
#  (10≤N≤99)
# .

# Output
# Print "YES" if the given number is lucky, otherwise print "NO".






n = int(input())

if 10<=10<=99:
 x = n%10
 n//=10
 y = n%10
 if(x%y==0 or y%x==0):
  print("YES")
 else:
  print("NO") 
else:  
 print("NO")