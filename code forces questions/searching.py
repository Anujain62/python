# Given a number N and an array A of N numbers. Determine if the number X exists in array A or not and print its position (0-index).
# Note: X may be found once or more than once and may not be found.

# Input
# First line contains a number N (1 ≤ N ≤ 105) number of elements.
# Second line contains N numbers (0 ≤ Ai ≤ 109).
# Third line contains a number X (0 ≤ X ≤ 109).

# Output
# Print the position of X in the first time you find it. If it doesn't exist print -1.



n = int(input())
lst = list(map(int,input().split()))
target = int(input())

idx = -1

for x in range(n):
 if lst[x]==target:
  idx=x
  break

print(idx)