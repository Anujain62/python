

l,r,m=map(int,input().split())
ans = 1
for i in range(l,r+1):
 ans = (ans*i)%m

print(ans)