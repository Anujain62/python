# Given a number N and an array A of N numbers. Print the array after doing the following operations:
# Replace every positive number by 1.
# Replace every negative number by 2.
# Input
# First line contains a number N (2 ≤ N ≤ 1000) number of elements.
# Second line contains N numbers (-105  ≤  Ai  ≤  105).

# Output
# Print the array after the replacement and it's values separated by space.




n = int(input())
lst = list(map(int,input().split()))

for i in range(n):
 if lst[i]<0:
  lst[i]=2
 elif lst[i]>0:
  lst[i]=1

for i in range(n):
 print(lst[i],end=" ")    