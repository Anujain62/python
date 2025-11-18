# Given two numbers A, B and a code S consisting of digits (0,1,2,...,9) and a symbol '-'.
# Determine if the code follows the following rules or not:

# The position A + 1 in the code is the symbol '-'.
# All other characters are one of the following digits: (0,1,2,...,9).

# Input
# First line contains two numbers A, B (1 ≤ A, B ≤ 10).
# Second line contains S (|S| = A + B + 1) and consists of '-' and digits from 0 through 9.

# Output
# Print "Yes" if the code S follows the above rules otherwise, print "No".




a,b = map(int,input().split())
s = input()
if s[a]!='-':
 print("No")
else:
 left = s[:a] 
 right = s[a+1:]
 if left.isdigit() and right.isdigit():
  print("Yes")
 else:
  print("No") 