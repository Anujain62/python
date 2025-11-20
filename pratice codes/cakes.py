T = int(input())   #no of cases

ans = []

for _ in range(T):
 N = int(input())   #no of lemon cakes
    
 if N <= 2:
  ans.append(N)
 else:
  ans.append((N//2)+1)

print("Answer : ")
for i in ans:
 print(i)  