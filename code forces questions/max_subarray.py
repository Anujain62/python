# A sub-array of array is an array composed from a contiguous block of the original array's elements.

# In other words A sub-array A[i-j], where (1 ≤ i ≤ j ≤ N), is a sequence of integers Ai, Ai + 1, ..., Aj.

# For Example :
# IF array = [1,6,3,7] then the subarrays are [1] , [6] , [3] , [7] , [1,6] , [6,3],[3,7], [1,6,3] , [6,3,7] , [1,6,3,7] .
# Something like [1,3] would not be a sub-array as it's not a contiguous subsection of the original array.
# Given a number N and an array A of N numbers. Print the maximum number of every sub-array separated by space.

# Input
# First line contains a number T (1 ≤ T ≤ 5) number of test cases.
# Each test case contains two lines:
# First line contains a number N (1 ≤ N ≤ 100) number of elements.
# Second line contains N numbers ( - 105 ≤ Ai ≤ 105).

# Output
# For each test case print a single line contains the maximum number of every sub-array separated by space.





t = int(input())

ans = []

for i in range(t):
 n = int(input())
 lst = list(map(int,input().split()))
 
 tempLst = []
 for i in range(n):
  mx = lst[i]
  for j in range(i,n):
   mx = max(mx,lst[j])
   tempLst.append(mx)
 ans.append(tempLst)  


for i in range(t):
 for j in range(len(ans[i])):
  print(ans[i][j],end=" ")
 print() 







