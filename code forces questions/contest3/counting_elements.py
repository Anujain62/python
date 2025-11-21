
n = int(input())
lst = list(map(int,input().split()))

count = 0
for i in lst:
 if i+1 in lst:
  count+=1

print(count)