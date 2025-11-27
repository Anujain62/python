

RA, CA = map(int, input().split())

A = []
for _ in range(RA):
 A.append(list(map(int, input().split())))

RB, CB = map(int, input().split())

B = []
for _ in range(RB):
 B.append(list(map(int, input().split())))

C = [[0] * CB for _ in range(RA)]

for i in range(RA):
 for j in range(CB):
  s = 0
  for k in range(CA):  
   s += A[i][k] * B[k][j]
  C[i][j] = s

for row in C:
 print(*row)




