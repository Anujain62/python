
# Given three numbers A, B, C. Print these numbers in ascending order followed by a blank line and then the values in the sequence as they were read.

# Input
# Only one line containing three numbers A, B, C ( - 106  ≤  A, B, C  ≤  106)

# Output
# Print the values in ascending order followed by a blank line and then the values in the sequence as they were read.


a,b,c = map(int,input().split())
nums = [a,b,c]
for i in sorted(nums):
 print(i)
print()
for i in nums:
 print(i) 