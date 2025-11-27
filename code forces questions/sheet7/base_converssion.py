
def to_binary(n):
 if n == 0:
  return ""
 return to_binary(n // 2) + str(n % 2)

t = int(input())
for _ in range(t):
 n = int(input())
 if n == 0:
  print(0)
 else:
  print(to_binary(n))

