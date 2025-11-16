# You are given a range represented by two integers L
#  and R
# , and you should find the sum of the numbers in the range between L
#  and R
#  inclusive.

# Input
# First line contains a number T
#  (1≤T≤105
# ) – the number of test cases.

# Each of the next T
#  lines contains two numbers L,R
#  (1≤L,R≤109
# ).

# Output
# For each test case, print the sum.







n = int(input())
m = n

lst = []
while n>0:
 tempLst = list(map(int,input().split()))
 lst.append(tempLst)
 n-=1

for i in lst:
 if(i[0]>i[1]):
  i[0],i[1] = i[1],i[0]
 # s[n] = (n*(n+1))/2
 sum = ((i[1]*(i[1]+1))//2) - (((i[0]-1)*i[0])//2)
 
 print(sum) 

