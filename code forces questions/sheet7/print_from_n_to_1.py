
def print_num(n):
 if n==0:
  return
 if(n==1):
  print(n)
 else: 
  print(n,end=" ")
 print_num(n-1)

n=int(input())
print_num(n)

