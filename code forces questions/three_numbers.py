# Given two numbers K and S. Determine how many different values of X,Y and Z such that (0≤X,Y,Z≤K) and X+Y+Z=S.

# Input
# Only one line containing two numbers K and S (0≤K≤3000,0≤S≤3K).

# Output
# Print the answer required above.



k,s = map(int,input().split())

count = 0
for x in range(k+1):
 for y in range(k+1):
  z=s-x-y
  if 0<=z<=k:
   count+=1

print(count)
