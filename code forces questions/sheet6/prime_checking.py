
n = int(input())
is_prime = True
if n < 2:
 print("NO")
elif n in (2, 3):
 print("YES")
elif n % 2 == 0 or n % 3 == 0:
 print("NO")
else:
 is_prime = True
 i = 5
 while i * i <= n:
  if n % i == 0 or n % (i + 2) == 0:
   is_prime = False
   break
  i += 6

 print("YES" if is_prime else "NO")
