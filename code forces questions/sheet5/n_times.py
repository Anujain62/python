

def n_times(n,ch):
 for i in range(n):
  print(ch,end=" ")


t=int(input())
for i in range(t):
 n,ch=input().split()
 n_times(int(n),ch)
 print()
