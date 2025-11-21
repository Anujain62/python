
n=int(input())
for i in range(n):
 s,t=input().split()
 result = ""
 x = min(len(s),len(t))
 for i in range(x):
  result += s[i]+t[i]
 
 result+=s[x:]
 result+=t[x:]

 print(result)
