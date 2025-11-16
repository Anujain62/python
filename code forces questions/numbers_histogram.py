
s = input()
n = int(input())
arr = list(map(int, input().split()))

for i in arr:
 for j in range(i):
  print(s,end="")
 print() 