
# Given a number N and an array A of N numbers. Print the array after doing the following operations:

# Find minimum number in these numbers.
# Find maximum number in these numbers.
# Swap minimum number with maximum number.
# Input
# First line contains a number N (2 ≤ N ≤ 1000) number of elements.

# Second line contains N numbers ( - 105 ≤ Ai ≤ 105)

# It's guaranteed that all numbers are distinct.

# Output
# Print the array after the replacement operation.




n = int(input())

lst = list(map(int,input().split()))

small = min(lst)
large = max(lst)

idx_small = 0
idx_large = 0
for i in range(n):
 if lst[i]==small:
  idx_small = i
 if lst[i]==large:
  idx_large = i

lst[idx_large],lst[idx_small] = lst[idx_small],lst[idx_large]

for i in lst:
 print(i,end=" ")
