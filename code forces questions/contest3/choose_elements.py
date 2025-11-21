
n,k = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort(reverse=True)
sum = 0
count = 0

for i in lst:
 if i>0 and count<k:
  sum+=i
  count+=1

print(sum)

