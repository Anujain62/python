
# Given 2 numbers N, M and an array A of N numbers. For every number from 1 to M, print how many times this number appears in this array.

# Input
# First line contains two numbers N, M (1≤N≤105,1≤M≤105).

# Second line contains N numbers (1≤Ai≤M).

# Output
# Print M lines, the ith line should contain number of times that the number i appears in A




n,m = map(int,input().split())
a = list(map(int,input().split()))

freq = []
tempLst = []
for i in a:
 if i in tempLst:
  continue
 tempLst.append(i)
 ans = a.count(i)
 freq.append(ans) 

for i in freq:
 print(i) 





