# Given a number N and an array A of N numbers. Determine if the array is lucky or not.

# Note: the array is lucky if the frequency (number of occurrence) of the minimum element is odd.

# Input
# First line contains a number N (2 ≤ N ≤ 1000) number of elements.
# Second line contains N numbers ( - 105 ≤ Ai ≤ 105).

# Output
# Print "Lucky" (without quotes) if the frequency of the minimum element is odd, otherwise print "Unlucky"(without quotes).




n = int(input())
lst = list(map(int,input().split()))

small = min(lst)
freq = lst.count(small)
if freq%2==1:
 print("Lucky")
else:
 print("Unlucky") 


