# a sub sequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# IF array = [1,6,3 , 7] then the some subsequences are [1,3,7] , [6,7] , [1] , [6,3,7] , [1,7] .

# Something like [3,1] and [6 , 7 , 1] would not be sub sequences of the array [1,6,3 , 7].

# Given 2 numbers N, M and 2 arrays A consists of N numbers and B consists of M numbers. Determine whether B is a sub-sequence of A or not.

# Note: The array B is called a sub-sequence of A if it's possible to remove zero or some elements from A to get B.

# For example: if A=[1,4,7], and B is [1], [1,4], [1,7],[1,4,7] or [4,7] then B is a sub-sequence of A.

# Input
# First line contains two numbers N,M (1≤N≤104,1≤M≤N) , the sizes of arrays A and B respectively.

# Second line contains N numbers (1≤Ai≤109) elements of array A.

# Third line contains M numbers (1≤Bi≤109) elements of array B.

# Output
# Print "YES" (without the quotes), if B
#  is a sub-sequence of A
#  otherwise, print "NO" (without the quotes).



a,b = map(int,input().split())

lstA = list(map(int,input().split()))
lstB = list(map(int,input().split()))

x = 0
for i in range(a):
 if x<b and lstA[i]==lstB[x]:
  x+=1

if x==b:
 print("YES")
else:
 print("NO") 
