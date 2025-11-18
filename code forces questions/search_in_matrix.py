# Given two numbers N and M, a 2D array of size N * M and a number X. Determine whether X exists in the 2D array A or not.

# Input
# First line contains two numbers N, M (2 ≤ N, M ≤ 100) N donates number of rows and M donates number of columns.

# Each of the next N lines will contain M numbers (1 ≤ Ai ≤ 105).

# Last line contains a number X (0 ≤ X ≤ 105) described above.

# Output
# Print "will take number" if the number doesn't exist in the 2D array otherwise, print "will not take number".



n,m = map(int,input().split())

lst = []
for i in range(n):
 tempLst = list(map(int,input().split()))
 lst.append(tempLst)

x = int(input()) 

found = False
for i in range(n):
 for j in range(m):
  if lst[i][j]==x:
   found=True
   break
 if found:
  break

if found:
 print("will not take number")
else:
  print("will take number")