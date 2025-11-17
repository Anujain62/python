# Given a number N and an array A of N numbers. Print the numbers after sorting them.

# Note:
# Don't use built-in-functions.
# try to solve it with bubble sort algorithm or Selection Sort.
# for more information watch : https://www.youtube.com/watch?v=EnodMqJuQEo.

# Input
# First line contains a number N (0 < N < 103) number of elements.
# Second line contains N numbers ( - 100 ≤ Ai ≤ 100).

# Output
# Print the numbers after sorting them.




n=int(input())
lst = list(map(int,input().split()))

for i in range(n-1):
 for j in range(i+1,n):
  if lst[i]>lst[j]:
   lst[i],lst[j]=lst[j],lst[i]

for x in lst:
 print(x,end=" ")



