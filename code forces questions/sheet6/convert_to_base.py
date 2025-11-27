
t = int(input())
N, X = map(int,input().split())

if t == 1:
 ans=0
 temp=0
 while N>0:
  mod=N%10
  power=mod*(X**temp)
  ans+=power
  temp+=1
  N//=10
 print(str(ans)) 


else:
 if N == 0:
  print(0)
 else:
  ans = ""
  while N > 0:
   rem = N % X
   if rem < 10:
    ans += str(rem)
   else:
    ans += chr(ord('A') + rem - 10)
   N //= X

  print(str(ans[::-1]))  