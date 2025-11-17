# Given a number N and an array A of N numbers. Determine if it's palindrome or not.

# Note:
# An array is called palindrome if it reads the same backward and forward, for example, arrays { 1 } and { 1,2,3,2,1 } are palindromes, while arrays { 1,12 } and { 4,7,5,4 } are not.

# Input
# First line contains a number N (1≤N≤105) number of elements.
# Second line contains N numbers (1≤Ai≤109).

# Output
# Print "YES" (without quotes) if A is a palindrome array, otherwise, print "NO" (without quotes).





n = int(input())
lst = list(map(int,input().split()))

left = 0
right =n-1
is_palin = True
while left<=right:
 if lst[left]!=lst[right]:
  is_palin = False
  break
 left+=1
 right-=1

if is_palin:
 print("YES")
else:
 print("NO") 





