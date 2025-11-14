# Given 4 numbers A
# , B
# , C
#  and D
# . Print the last 2 digits from their Multiplication.

# Input
# Only one line containing four numbers A
# , B
# , C
#  and D
#  (2≤A,B,C,D≤109)
# .

# Output
# Print the last 2 digits from their Multiplication



a, b, c, d = map(int, input().split())
result = ((a % 100) * (b % 100) * (c % 100) * (d % 100)) % 100
if(result<10):
 print("0"+str(result))
else:
 print(result) 

