
# Let's define f(x)
#  as the number of times at which the integer x
#  can be divided by 2
# .

# You are given N
#  numbers, and you should print the maximum f(x)
#  among all these numbers.

# Input
# The first line contains one number N
#  (1≤N≤105
# ).

# The second line contains N
#  space-separated numbers where each number is between 1
#  and 1018
#  (inclusive).

# Output
# Print the maximum f(x)
#  among all numbers.



n = int(input())

lst = list(map(int,input().split()))
count=0

for i in lst:
 x = 0
 while i>0:
  if i%2==0:
   i//=2
   x+=1
  else:
   break 
 if(x>count):
  count=x 

print(count)


