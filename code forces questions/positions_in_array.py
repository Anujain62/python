
# Given a number N and an array A of N numbers. Print all array positions that store a number less than or equal to 10 and the number stored in that position.

# Input
# First line contains a number N (2 ≤ N ≤ 1000) number of elements.
# Second line contains N numbers (-105  ≤  Ai  ≤  105).
# it's guaranteed that there is at least one number in array less than or equal to 10.

# Output
# For each number in the array that is equal to or less than 10 print a single line contains "A[i] = X", where i is the position in the array and X is the number stored in the position.



n = int(input())
lst = list(map(int,input().split()))

for i in range(n):
 if lst[i]<=10:
  print(f"A[{i}] = {lst[i]}")
