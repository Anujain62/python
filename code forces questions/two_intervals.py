
# Given the boundaries of 2 intervals. Print the boundaries of their intersection.

# Note: Boundaries mean the two ends of an interval which are the starting number and the ending number.

# Input
# Only one line contains two intervals [l1,r1]
# , [l2,r2]
#  where (1≤l1,l2,r1,r2≤109)
# , (l1≤r1,l2≤r2)

# It's guaranteed that l1≤r1 and l2≤r2 




l1,r1,l2,r2 = map(int,input().split())
left = max(l1,l2)  
right=min(r1,r2)
if(left<=right):
 print(left,right)
else:
 print("-1") 
