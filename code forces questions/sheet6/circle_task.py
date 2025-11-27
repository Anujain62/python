
X, Y, R, N = map(int, input().split())

R2 = R * R 
for _ in range(N):
 x, y = map(int, input().split())
    
 dist2 = (x - X) ** 2 + (y - Y) ** 2
    
 if dist2 <= R2:
  print("YES")
 else:
  print("NO")
