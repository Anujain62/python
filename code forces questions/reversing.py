# Given a number N and an array A of N numbers. Print the array in a reversed order.

# Note:
# *Don't use built-in-functions.

# Input
# First line contains a number N (1 ≤ N ≤ 103) number of elements.
# Second line contains N numbers (0 ≤ Ai ≤ 109).

# Output
# Print the array in a reversed order.




n = int(input())
lst = list(map(int,input().split()))

newlst = []
for i in range(n-1,-1,-1):
 newlst.append(lst[i])

for i in newlst:
 print(i,end=" ") 


