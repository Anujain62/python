# A sub-array of array is an array composed from a contiguous block of the original array's elements.

# In other words A sub-array A[i-j], where (1 ≤ i ≤ j ≤ N), is a sequence of integers Ai, Ai + 1, ..., Aj.

# For Example :

# IF array = [1,6,3,7] then the subarrays are [1] , [6] , [3] , [7] , [1,6] , [6,3],[3,7], [1,6,3] , [6,3,7] , [1,6,3,7] .
# Something like [1,3] would not be a sub-array as it's not a contiguous subsection of the original array.
# Given a number N and an array A of N numbers. Print the number of sub-arrays which are non-decreasing.
# Note:
# A sub-array A[i-j] is non-decreasing if (Ai  ≤  Ai + 1  ≤  Ai + 2  ≤  ...  ≤  Aj).
# Input
# First line contains a number T (1 ≤ T ≤ 5) number of test cases.
# Each test case contains two lines:
# First line contains a number N (1 ≤ N ≤ 102) number of elements.
# Second line contains N numbers ( - 105 ≤ Ai ≤ 105)

# Output
# For each test case print a single line contains the number of sub-arrays which are non-decreasing..



t = int(input())

for _ in range(t):
 n = int(input())
 arr = list(map(int, input().split()))

 count = 0
 length = 1   

 for i in range(1, n):
  if arr[i] >= arr[i-1]:     
   length += 1
  else:
   count += length * (length + 1) // 2
   length = 1
 count += length * (length + 1) // 2

 print(count)
