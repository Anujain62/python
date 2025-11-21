# Given two numbers N, M and a 2D array of size N * M. Print the inverted array that appeared in the mirror.

# Input
# First line contains two numbers N, M (1≤N,M≤100) N donates number of rows and M donates number of columns.

# Each of the next N lines will contain M numbers (1≤Ai,j≤109).

# Output
# Print the inverted array.



n,m = map(int,input().split())

matrix = []
for i in range(n):
 temp = list(map(int,input().split()))
 matrix.append(temp)

for i in range(n):
 for j in reversed(matrix[i]):
  print(j,end=" ") 
 print() 



