
def can_reach(n):
 if n == 1:
  return True
 if n < 1:
  return False

 ok = False
 if n % 10 == 0:
  ok |= can_reach(n // 10)
 if n % 20 == 0:
  ok |= can_reach(n // 20)
 return ok


t = int(input())
for _ in range(t):
 n = int(input())
 print("YES" if can_reach(n) else "NO")
