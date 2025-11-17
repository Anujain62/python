# Given a number N and an array A of N numbers. Print the absolute summation of these numbers.
# absolute value : means to remove any negative sign in front of a number .
# EX : |-5| = 5 , |7| = 7

# Input
# First line contains a number N (1 ≤ N ≤ 105) number of elements.
# Second line contains N numbers (-109  ≤  Ai  ≤  109).

# Output
# Print the absolute summation of these numbers.



n = int(input())

lst = list(map(int,input().split()))
sum = 0
for i in lst:
 sum+=i

if(sum<0):
 sum*=(-1)

print(sum)



