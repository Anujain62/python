
# You are given two integers n and s, and you have to find distinct positive integers, such that each of them is ≤n, and their summation =s. Otherwise, state that this is impossible.

# Input
# The first line contains a number T
#  (1≤T≤100) – number of test cases.

# Each of the next T lines contains two space-separated integers n,s
#  (1≤n≤105,1≤s≤1018).

# Output
# For each test case, if there is no possible answer, print −1
#  on a single line. Otherwise, print the set of numbers that satisfy the above condition on a single line. You can print the numbers in any order. If there are multiple answers, you can print any of them.




n = int(input())
lst = []
for i in range(n):
 tempLst = list(map(int,input().split()))
 lst.append(tempLst)

for x in lst:
 sum = x[1]
 limit = x[0]
 ans = []
 t = 0
 for i in range(limit,0,-1):
  if t+i<=sum:
   ans.append(i)
   t+=i
 if t==sum:
   print(*ans) 
 else:
   print(-1)  
