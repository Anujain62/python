
n = int(input())

fibo1 = 0
fibo2 = 1
if n==0:
 print(fibo1)
else:
 for i in range(n): 
  print(fibo1,end=" ")
  temp=fibo1+fibo2
  fibo1=fibo2
  fibo2=temp 