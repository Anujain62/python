

n = int(input())
lst = list(map(int,input().split()))

for i in range(0,n):
 if lst[i]==0:
  lst[:i] = reversed(lst[:i])

print(*lst)